"""The page uses only named origins (#17; SECURITY.md, "In scope").

Run: python3 -m unittest discover -s tests
Standard library only.
"""

import re
import unittest
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parent.parent
PAGE = (ROOT / "index.html").read_text(encoding="utf-8")

# Adding an origin is a security-related change (AGENTS.md).
ALLOWED = {"https://fonts.googleapis.com"}

ATTRIBUTE_URL = re.compile(r"""\b(?:href|src)\s*=\s*(["'])((?:https?:)?//.*?)\1""", re.IGNORECASE)
CSS_URL = re.compile(r"""\burl\(\s*(["']?)((?:https?:)?//.*?)\1\s*\)""", re.IGNORECASE)
IMPORT_URL = re.compile(r"""@import\s+(["'])((?:https?:)?//.*?)\1""", re.IGNORECASE)


def absolute_urls(page):
    """Absolute and scheme-relative URLs in HTML attributes and CSS."""
    urls = []
    for pattern in (ATTRIBUTE_URL, CSS_URL, IMPORT_URL):
        urls.extend(match.group(2) for match in pattern.finditer(page))
    return urls


def origin(url):
    """Reduce an absolute or scheme-relative URL to scheme://netloc."""
    if url.startswith("//"):
        url = f"https:{url}"
    parts = urlsplit(url)
    return f"{parts.scheme}://{parts.netloc}"


class PageOrigins(unittest.TestCase):
    def test_every_origin_is_allowed(self):
        for url in absolute_urls(PAGE):
            with self.subTest(url=url):
                self.assertIn(origin(url), ALLOWED)

    def test_the_allow_list_is_used(self):
        used = {origin(url) for url in absolute_urls(PAGE)}
        for allowed in ALLOWED:
            with self.subTest(origin=allowed):
                self.assertIn(allowed, used)


if __name__ == "__main__":
    unittest.main()
