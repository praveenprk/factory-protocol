"""Checks on the page (DECISION-002, TEST gate; V-ENG-008-03).

Run: python3 -m unittest discover -s tests
Standard library only.
"""

import re
import unittest
from itertools import pairwise
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGE = (ROOT / "index.html").read_text(encoding="utf-8")
README = (ROOT / "README.md").read_text(encoding="utf-8")

STATION = re.compile(r'\{\s*g:\s*"([A-Z-]+)",\s*n:\s*"(\d\d)",\s*from:\s*"([^"]+)"')


def stations():
    """(name, number, gate) for each station in the inline script's S array."""
    return STATION.findall(PAGE)


def readme_line():
    """The station sequence README.md states under 'The line'."""
    m = re.search(r"`(INTAKE(?: → [A-Z-]+)+)`", README)
    if m is None:
        raise AssertionError("README.md has no `INTAKE → … → CLOSED` line")
    return m.group(1).split(" → ")


class PageIsADocument(unittest.TestCase):
    def test_index_html_is_a_complete_english_document(self):
        self.assertTrue(PAGE.startswith("<!doctype html>"))
        self.assertIn('<html lang="en">', PAGE)
        self.assertIn('<meta charset="utf-8" />', PAGE)
        self.assertTrue(PAGE.rstrip().endswith("</html>"))


class StationsMatchTheLine(unittest.TestCase):
    def test_script_has_eleven_stations_numbered_00_to_10(self):
        self.assertEqual([n for _, n, _ in stations()], [f"{i:02d}" for i in range(11)])

    def test_script_stations_are_the_readme_line_in_order(self):
        self.assertEqual([g for g, _, _ in stations()], readme_line())

    def test_each_gate_is_the_previous_station_to_this_one(self):
        got = stations()
        self.assertEqual(got[0][2], "start")
        for (prev, _, _), (name, _, gate) in pairwise(got):
            with self.subTest(station=name):
                self.assertEqual(gate, f"{prev}→{name}")


class PageReferences(unittest.TestCase):
    def test_every_in_page_link_has_a_target(self):
        ids = set(re.findall(r'\bid="([^"]+)"', PAGE))
        for target in re.findall(r'href="#([^"]+)"', PAGE):
            with self.subTest(target=target):
                self.assertIn(target, ids)

    def test_every_element_the_script_looks_up_exists(self):
        ids = set(re.findall(r'\bid="([^"]+)"', PAGE))
        for target in re.findall(r'getElementById\("([^"]+)"\)', PAGE):
            with self.subTest(target=target):
                self.assertIn(target, ids)

    def test_page_loads_no_external_script(self):
        self.assertIsNone(re.search(r"<script[^>]*\bsrc=", PAGE, re.I))

    def test_external_links_use_https(self):
        for url in re.findall(r'(?:href|src)="(http[^"]*)"', PAGE):
            with self.subTest(url=url):
                self.assertTrue(url.startswith("https://"))


if __name__ == "__main__":
    unittest.main()
