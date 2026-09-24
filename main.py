"""Main entry point: launches CLI or GUI based on arguments."""

from __future__ import annotations

import sys


def main() -> None:
    """Entry point that dispatches to CLI or GUI."""
    if len(sys.argv) > 1 and sys.argv[1] == "--gui":
        from src.gui import main as gui_main

        gui_main()
    else:
        from src.cli import main as cli_main

        sys.exit(cli_main())


if __name__ == "__main__":
    main()
