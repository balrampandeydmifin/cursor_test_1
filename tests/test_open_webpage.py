"""Tests for open_webpage.py (browser is mocked; nothing actually opens)."""

import io
import sys
import unittest
from unittest.mock import patch

import open_webpage


class TestOpenWebpage(unittest.TestCase):
    def test_default_url_opens_example(self):
        with patch.object(sys, "argv", ["open_webpage.py"]), patch(
            "open_webpage.webbrowser.open", return_value=True
        ) as mock_open:
            rc = open_webpage.main()
        self.assertEqual(rc, 0)
        mock_open.assert_called_once_with("https://example.com", new=0, autoraise=True)

    def test_custom_url(self):
        with patch.object(sys, "argv", ["open_webpage.py", "https://example.org"]), patch(
            "open_webpage.webbrowser.open", return_value=True
        ) as mock_open:
            rc = open_webpage.main()
        self.assertEqual(rc, 0)
        mock_open.assert_called_once_with("https://example.org", new=0, autoraise=True)

    def test_url_is_stripped(self):
        with patch.object(
            sys, "argv", ["open_webpage.py", "  https://trimmed.test  "]
        ), patch("open_webpage.webbrowser.open", return_value=True) as mock_open:
            rc = open_webpage.main()
        self.assertEqual(rc, 0)
        mock_open.assert_called_once_with("https://trimmed.test", new=0, autoraise=True)

    def test_new_window_flag(self):
        with patch.object(
            sys, "argv", ["open_webpage.py", "-n", "1", "https://a.test"]
        ), patch("open_webpage.webbrowser.open", return_value=True) as mock_open:
            rc = open_webpage.main()
        self.assertEqual(rc, 0)
        mock_open.assert_called_once_with("https://a.test", new=1, autoraise=True)

    def test_new_tab_flag(self):
        with patch.object(
            sys, "argv", ["open_webpage.py", "-n", "2", "https://a.test"]
        ), patch("open_webpage.webbrowser.open", return_value=True) as mock_open:
            rc = open_webpage.main()
        self.assertEqual(rc, 0)
        mock_open.assert_called_once_with("https://a.test", new=2, autoraise=True)

    def test_empty_url_returns_error(self):
        stderr = io.StringIO()
        with patch.object(sys, "argv", ["open_webpage.py", "   "]), patch(
            "open_webpage.webbrowser.open"
        ) as mock_open:
            with patch.object(sys, "stderr", stderr):
                rc = open_webpage.main()
        self.assertEqual(rc, 1)
        mock_open.assert_not_called()
        self.assertIn("empty URL", stderr.getvalue())

    def test_browser_open_failure_returns_error(self):
        stderr = io.StringIO()
        with patch.object(sys, "argv", ["open_webpage.py", "https://x.com"]), patch(
            "open_webpage.webbrowser.open", return_value=False
        ):
            with patch.object(sys, "stderr", stderr):
                rc = open_webpage.main()
        self.assertEqual(rc, 1)
        self.assertIn("Could not open browser", stderr.getvalue())


if __name__ == "__main__":
    unittest.main()
