"""
# test_misc_str.py

"""
import logging
import unittest

from ml.misc.str import check_match_patterns
from ml.utils.logger import get_logger

LOGGER = get_logger(__name__)


class MiscStrTests(unittest.TestCase):
    """
    MiscStrTests includes all unit tests for ml.misc.str module
    """
    @classmethod
    def teardown_class(cls):
        logging.shutdown()

    def setUp(self):
        """setup for test"""
        pass

    def tearDown(self):
        """tearing down at the end of the test"""
        pass

    def test_check_match_patterns(self):
        """
        test.ml.misc.str :: check_match_patterns
        """
        tests = [
            {"p": "", "s": "", "expected": True},
            {"p": "abab", "s": "testmetestme", "expected": True},
            {"p": "abba", "s": "testmetestme", "expected": False},
            {"p": "abcab", "s": "testmetometest", "expected": True},
        ]
        for test in tests:
            p = test.get("p")
            s = test.get("s")
            expected = test.get("expected")
            result = check_match_patterns(p, s)
            self.assertEqual(result, expected)
        pass