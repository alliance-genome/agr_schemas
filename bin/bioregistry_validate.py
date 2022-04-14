"""Test that all prefixes are alignable with the Bioregistry."""

import unittest
from pathlib import Path

import bioregistry
import yaml

HERE = Path(__file__).parent.resolve()
ROOT = HERE.parent.resolve()
PATH = ROOT.joinpath("resourceDescriptors.yaml")


class TestIntegrity(unittest.TestCase):
    def setUp(self) -> None:
        self.entries = yaml.safe_load(PATH.read_text())

    def test_prefixes(self):
        for entry in self.entries:
            prefix = entry["db_prefix"]
            with self.subTest(prefix=prefix):
                self.assertIsNotNone(bioregistry.normalize_prefix(prefix), msg=f"Prefix {prefix} is not in bioregistry")
                for alias in entry.get("aliases", []):
                    self.assertIsNotNone(bioregistry.normalize_prefix(alias), msg=f"Unknown alias {alias} for prefix {prefix}")
