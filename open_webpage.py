#!/usr/bin/env python3
"""Open a URL in the system's default web browser."""

import argparse
import sys
import webbrowser


def main() -> int:
    parser = argparse.ArgumentParser(description="Open a webpage in your default browser.")
    parser.add_argument(
        "url",
        nargs="?",
        default="https://example.com",
        help="URL to open (default: https://example.com)",
    )
    parser.add_argument(
        "-n",
        "--new",
        type=int,
        choices=(0, 1, 2),
        default=0,
        metavar="N",
        help="0=default tab, 1=new window, 2=new tab (if supported)",
    )
    args = parser.parse_args()

    url = args.url.strip()
    if not url:
        print("Error: empty URL", file=sys.stderr)
        return 1

    opened = webbrowser.open(url, new=args.new, autoraise=True)
    if not opened:
        print(f"Could not open browser for: {url}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
