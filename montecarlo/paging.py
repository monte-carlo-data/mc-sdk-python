# Hand-written, not generator output.
"""Walking a paginated list.

A paginated list method returns one page at a time: a model carrying `items`, `next_cursor`,
`has_more` and `count`. `paginate` calls such a method repeatedly, follows the cursor, and
yields every item across every page.

One function serves every paginated list, because a page is recognised by its attributes rather
than by its type. The Go SDK generates an `All` method per list instead, where the attributes
are not reachable without knowing the type.
"""

from __future__ import annotations

from collections.abc import Callable, Iterator
from typing import Any, Protocol, TypeVar

T = TypeVar("T")


class PaginationError(Exception):
    """A page the walk cannot continue from."""


class NoCursorError(PaginationError):
    """The API reported more pages and supplied no cursor to ask for the next one."""


class RepeatedCursorError(PaginationError):
    """The API returned a cursor it had already served, which would repeat a page forever."""


class Page(Protocol[T]):
    """One page of a paginated list, as every `Paged<Model>Out` the generator emits."""

    items: list[T]
    next_cursor: str | None
    has_more: bool


def paginate(list_page: Callable[..., Page[T]], **kwargs: Any) -> Iterator[T]:
    """Yield every item of a paginated list, following the cursor from page to page.

    `list_page` is a paginated list method, such as `WarehousesApi(client).list_warehouses`.
    Remaining keyword arguments go to every call, so a filter applies to the whole walk. A
    `cursor` among them is where the walk starts.

    The walk ends when a page reports no more pages. An error from `list_page` propagates, so a
    failed request ends the walk on the exception the client raised. Two malformed pages end it
    instead: more pages promised with no cursor raises `NoCursorError`, and a cursor already
    requested raises `RepeatedCursorError`. A server repeating a cursor would otherwise keep a
    caller in this loop forever.

    Each call asks for whatever page size `list_page` defaults to. Passing `limit` — the largest
    the operation accepts — walks the same list in fewer requests.
    """
    cursor = kwargs.pop("cursor", None)
    requested: set[str | None] = set()
    while True:
        requested.add(cursor)
        page = list_page(cursor=cursor, **kwargs)
        yield from page.items
        if not page.has_more:
            return
        if not page.next_cursor:
            raise NoCursorError("the API reported more items but returned no cursor")
        if page.next_cursor in requested:
            raise RepeatedCursorError("the API returned the same cursor twice")
        cursor = page.next_cursor
