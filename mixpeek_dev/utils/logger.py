"""Logging utilities with rich formatting.

This module provides beautiful console output using the rich library.

**Features:**
- Color-coded output (success=green, error=red, warning=yellow)
- Progress indicators
- Formatted tables for results
- LLM-friendly error messages
"""

from typing import Any, Dict, List, Optional

try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.progress import Progress, SpinnerColumn, TextColumn

    HAS_RICH = True
except ImportError:
    HAS_RICH = False


class Logger:
    """Logger with rich formatting support.

    Falls back to plain text if rich is not installed.

    **Example:**

    ```python
    logger = Logger()
    logger.success("Plugin loaded successfully")
    logger.error("Failed to load manifest.py")
    logger.info("Running tests...")
    ```
    """

    def __init__(self):
        """Initialize logger."""
        if HAS_RICH:
            self.console = Console()
        else:
            self.console = None

    def success(self, message: str):
        """Print success message in green.

        Args:
            message: Success message
        """
        if self.console:
            self.console.print(f"✓ {message}", style="bold green")
        else:
            print(f"✓ {message}")

    def error(self, message: str):
        """Print error message in red.

        Args:
            message: Error message
        """
        if self.console:
            self.console.print(f"✗ {message}", style="bold red")
        else:
            print(f"✗ {message}")

    def warning(self, message: str):
        """Print warning message in yellow.

        Args:
            message: Warning message
        """
        if self.console:
            self.console.print(f"⚠ {message}", style="bold yellow")
        else:
            print(f"⚠ {message}")

    def info(self, message: str):
        """Print info message.

        Args:
            message: Info message
        """
        if self.console:
            self.console.print(message)
        else:
            print(message)

    def print_results_table(self, results: List[Dict[str, Any]], title: str = "Results"):
        """Print results in a formatted table.

        Args:
            results: List of result dicts
            title: Table title
        """
        if not results:
            self.info("No results to display")
            return

        if self.console:
            table = Table(title=title)

            # Add columns from first result
            for key in results[0].keys():
                table.add_column(key.replace("_", " ").title(), style="cyan")

            # Add rows
            for result in results:
                table.add_row(*[str(v) for v in result.values()])

            self.console.print(table)
        else:
            # Fallback to plain text
            print(f"\n{title}")
            print("=" * len(title))
            for result in results:
                for key, value in result.items():
                    print(f"{key}: {value}")
                print()


def get_logger() -> Logger:
    """Get a logger instance.

    Returns:
        Logger instance

    Example:
        ```python
        from mixpeek_dev.utils import get_logger

        logger = get_logger()
        logger.success("Test passed!")
        ```
    """
    return Logger()
