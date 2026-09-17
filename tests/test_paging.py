"""Tests for `montecarlo.paging`."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import pytest

from montecarlo import WarehousesApi, new_client
from montecarlo.auth import Options
from montecarlo.paging import (
    NoCursorError,
    PaginationError,
    RepeatedCursorError,
    paginate,
)
from tests.conftest import FakeApi


@dataclass
class CannedPage:
    """One page a FakeList replays. `has_more` and `next_cursor` are independent, so a canned
    page can claim more pages than it has a cursor for."""

    items: list[str]
    next_cursor: str | None = None
    has_more: bool = False


@dataclass
class FakeList:
    """A paginated list method that replays canned pages and records the cursor each call
    received. A call past the last page raises, so a walk that over-fetches fails on that
    rather than on an index error."""

    pages: list[CannedPage]
    asked: list[str | None] = field(default_factory=list)

    def __call__(self, cursor: str | None = None, **kwargs: object) -> CannedPage:
        self.asked.append(cursor)
        index = len(self.asked) - 1
        if index >= len(self.pages):
            raise AssertionError(
                f"the walk asked for page {index + 1}, only {len(self.pages)} are canned"
            )
        return self.pages[index]


def test_a_walk_yields_every_page_in_order() -> None:
    listing = FakeList(
        [
            CannedPage(["a", "b"], next_cursor="c1", has_more=True),
            CannedPage(["c"], next_cursor="c2", has_more=True),
            CannedPage(["d", "e"]),
        ]
    )

    assert list(paginate(listing)) == ["a", "b", "c", "d", "e"]
    assert listing.asked == [None, "c1", "c2"]


def test_a_page_reporting_no_more_ends_the_walk_whatever_cursor_it_carries() -> None:
    """`has_more` is the terminator, not the cursor's presence. A last page that still carries
    a cursor is the shape that tells the two apart, and `FakeList` raises on the over-fetch a
    cursor-driven loop would make."""
    listing = FakeList([CannedPage(["a"], next_cursor="c1", has_more=False)])

    assert list(paginate(listing)) == ["a"]
    assert listing.asked == [None]


def test_a_walk_stops_fetching_when_the_consumer_stops() -> None:
    listing = FakeList([CannedPage(["a", "b"], next_cursor="c1", has_more=True)])

    for _ in paginate(listing):
        break

    assert listing.asked == [None]


def test_a_walk_passes_its_other_arguments_to_every_call() -> None:
    seen: list[dict[str, object]] = []

    def listing(cursor: str | None = None, **kwargs: object) -> CannedPage:
        seen.append(kwargs)
        if cursor is None:
            return CannedPage(["a"], next_cursor="c1", has_more=True)
        return CannedPage(["b"])

    list(paginate(listing, limit=100, warehouse_id="w1"))

    assert seen == [{"limit": 100, "warehouse_id": "w1"}] * 2


def test_a_walk_asks_for_the_largest_page_the_api_serves() -> None:
    seen: list[dict[str, object]] = []

    def listing(cursor: str | None = None, **kwargs: object) -> CannedPage:
        seen.append(kwargs)
        return CannedPage(["a"])

    list(paginate(listing))

    assert seen == [{"limit": 100}]


def test_a_walk_does_not_ask_the_server_for_a_total() -> None:
    seen: list[dict[str, object]] = []

    def listing(cursor: str | None = None, **kwargs: object) -> CannedPage:
        seen.append(kwargs)
        return CannedPage(["a"])

    list(paginate(listing, with_count=True))

    assert "with_count" not in seen[0]


def test_a_cursor_argument_is_where_the_walk_starts() -> None:
    listing = FakeList([CannedPage(["a"])])

    list(paginate(listing, cursor="resume-here"))

    assert listing.asked == ["resume-here"]


def test_more_pages_with_no_cursor_is_refused() -> None:
    listing = FakeList([CannedPage(["a"], has_more=True)])

    with pytest.raises(NoCursorError, match="no cursor") as failure:
        list(paginate(listing))
    assert isinstance(failure.value, PaginationError)


def test_a_repeated_cursor_is_refused() -> None:
    def listing(cursor: str | None = None, **kwargs: object) -> CannedPage:
        return CannedPage(["a"], next_cursor="same", has_more=True)

    with pytest.raises(RepeatedCursorError, match="same cursor twice") as failure:
        list(paginate(listing))
    assert isinstance(failure.value, PaginationError)


def test_a_cursor_repeated_after_other_pages_is_refused() -> None:
    """Every cursor is remembered, not just the last one, so a server cycling through several
    cursors is caught as surely as one repeating a single cursor."""
    cursors = iter(["c1", "c2", "c1"])

    def listing(cursor: str | None = None, **kwargs: object) -> CannedPage:
        return CannedPage(["a"], next_cursor=next(cursors), has_more=True)

    with pytest.raises(RepeatedCursorError):
        list(paginate(listing))


def test_a_failed_request_ends_the_walk_on_its_own_exception() -> None:
    boom = RuntimeError("boom")

    def listing(cursor: str | None = None, **kwargs: object) -> CannedPage:
        if cursor is None:
            return CannedPage(["a"], next_cursor="c1", has_more=True)
        raise boom

    walk = paginate(listing)

    assert next(walk) == "a"
    with pytest.raises(RuntimeError) as failure:
        next(walk)
    assert failure.value is boom


def test_an_empty_list_yields_nothing() -> None:
    listing = FakeList([CannedPage([])])

    assert list(paginate(listing)) == []
    assert listing.asked == [None]


DEPLOYMENT_ID = "00000000-0000-4000-8000-000000000002"


def _warehouse_page(
    labels: list[str], next_cursor: str | None, has_more: bool
) -> dict[str, object]:
    """One page of the warehouses list as the API serves it, carrying every field the generated
    models require. `id` and `deployment_id` are UUID-typed, so a label becomes the last digit
    of one rather than standing in for it."""
    return {
        "items": [
            {
                "id": f"00000000-0000-4000-8000-00000000000{label}",
                "name": f"warehouse-{label}",
                "type": "bigquery",
                "deployment_id": DEPLOYMENT_ID,
                "created_time": "2026-09-17T00:00:00Z",
            }
            for label in labels
        ],
        "next_cursor": next_cursor,
        "has_more": has_more,
        "count": None,
    }


def test_a_walk_through_the_generated_client_follows_the_cursor(
    isolate: Path, fake_api: FakeApi
) -> None:
    """Exercises a real generated list method rather than a fake, so the page model's attributes
    are the generator's own rather than this file's idea of them."""
    fake_api.api_responses = [
        _warehouse_page(["1", "2"], "c1", True),
        _warehouse_page(["3"], None, False),
    ]
    client = new_client(
        Options(
            endpoint=fake_api.url,
            token_id="id",
            token_secret="secret",
            config_dir=isolate,
        )
    )

    names = [w.name for w in paginate(WarehousesApi(client).list_warehouses)]

    assert names == ["warehouse-1", "warehouse-2", "warehouse-3"]
    cursors = [r.path.split("cursor=")[1].split("&")[0] for r in fake_api.api_requests()[1:]]
    assert cursors == ["c1"]


def test_a_malformed_page_from_the_generated_client_is_refused(
    isolate: Path, fake_api: FakeApi
) -> None:
    """`paginate` reads `next_cursor` off the generated model, so a null cursor has to reach it
    as a falsy value for the guard to fire."""
    fake_api.api_response = _warehouse_page(["1"], None, True)
    client = new_client(
        Options(
            endpoint=fake_api.url,
            token_id="id",
            token_secret="secret",
            config_dir=isolate,
        )
    )

    with pytest.raises(NoCursorError, match="no cursor"):
        list(paginate(WarehousesApi(client).list_warehouses))
