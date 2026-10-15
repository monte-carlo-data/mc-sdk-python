---
description: Coding standards for this repo
globs: "**/*"
---

# General Standards

Almost everything under `pycarlo2/` is `openapi-generator` output. The hand-written surface is
`pycarlo2/auth.py`, `oauth.py`, `profile.py`, `paging.py`, the tests under `tests/`, `tools/`,
`pyproject.toml`, `.openapi-generator-ignore`, and the repository documentation; see AGENTS.md
for the exact list. These rules apply to that surface. Do not hand-edit generated files: the
next generation run overwrites them.

## Code Style

- Keep functions small and focused on a single responsibility
- Prefer explicit over implicit; name things clearly
- Write code that reads like a specification
- Every hand-written module under `pycarlo2/` starts with `# Hand-written, not generator
  output.`; CI asserts it, and derives the generator-protection check from it. The
  `# Copyright Monte Carlo AI, Inc.` and `# SPDX-License-Identifier: Apache-2.0` lines follow
  it; test modules start with them.
- A hand-written identifier must never take a name the generator could emit: `<Schema>` for
  every schema in the spec, the `*Api` classes, `ApiClient`, `ApiResponse`, `Configuration`,
  and the exception classes

## Testing

- Tests live in `tests/`, one module per hand-written module, plus `test_public_surface.py`,
  which pins the generated `__init__.py`'s re-export of the hand-written names, and
  `conftest.py`
- The hand-written code's boundaries are the filesystem and an OAuth endpoint. Use `tmp_path`
  and the loopback HTTP server fixture rather than mocks
- Any test that builds a client or resolves options must use the `isolate` fixture and pass the
  directory it returns as `Options.config_dir`, so the test cannot read the developer's real
  credentials
- Use `monkeypatch` for environment variables
- Name a test for the invariant it pins, not for the function it calls

## Error Handling

- Handle errors at system boundaries: the credentials file, the OAuth exchange, anything a caller
  supplies. Raise `CredentialsError` for all of them
- Never put the contents of a credentials file, or a credential, in an error message or a
  chained exception; callers render these into unredacted surfaces
- Don't add error handling for scenarios that can't happen

## Verification

`uv run ruff check .`, `uv run ruff format --check .`, `uv run pyright`, `uv run pytest`.
