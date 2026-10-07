# Hand-written, not generator output.
# Copyright Monte Carlo AI, Inc.
# SPDX-License-Identifier: Apache-2.0
"""Walking a paginated list.

A paginated list method returns one page at a time: a model carrying `items`, `next_cursor`,
`has_more` and `count`. `paginate` calls such a method repeatedly, follows the cursor, and
yields every item across every page.

One function serves every paginated list, because a page is recognised by its attributes rather
than by its type. The Go SDK generates an `All` method per list instead, where the attributes
are not reachable without knowing the type.

These names stay in this module rather than joining the package root, which holds the generated
surface plus the three names a client cannot be built without. Pagination is one optional
feature, and a name kept out of the generated `__all__` is one no future schema can collide
with.
"""

from __future__ import annotations

from collections.abc import Callable, Iterator
from typing import Any, Protocol, TypeVar

T = TypeVar("T")

# Every paginated operation in the spec declares this same ceiling, so a walk asks for it rather
# than settling for the API's smaller default. An operation that ever lowers its own maximum
# rejects this value on the first call, which fails loudly rather than truncating a page.
_PAGE_LIMIT = 100


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
    `cursor` among them is where the walk starts. `limit` sets the page size and defaults to the
    largest the API serves; `with_count` is dropped, since a walk yields every item and never
    reports the total it would pay for.

    The walk ends when a page reports no more pages, when an error from `list_page` propagates,
    or when a malformed page raises `NoCursorError` or `RepeatedCursorError` rather than
    looping. Those guards catch a server repeating a cursor, not one minting a fresh cursor
    forever: bound a walk of unknown length from the consumer, with `itertools.islice` or a
    timeout among the keyword arguments.
    """
    cursor = kwargs.pop("cursor", None)
    kwargs.pop("with_count", None)
    kwargs.setdefault("limit", _PAGE_LIMIT)
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
