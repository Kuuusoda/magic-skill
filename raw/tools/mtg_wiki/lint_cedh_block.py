#!/usr/bin/env python3
"""Backward-compatible shim for the generalized strategy block linter."""

from lint_strategy_block import main


if __name__ == "__main__":
    raise SystemExit(main())
