import unittest

from pycheck import all_valid, is_int, is_non_empty, is_number


class TestCore(unittest.TestCase):
    def test_int(self):
        self.assertTrue(is_int(3))
        self.assertFalse(is_int(True))

    def test_number(self):
        self.assertTrue(is_number(3.5))
        self.assertFalse(is_number("3.5"))

    def test_non_empty(self):
        self.assertTrue(is_non_empty("x"))
        self.assertFalse(is_non_empty(""))

    def test_all_valid(self):
        self.assertTrue(all_valid([1, 2, 3], is_int))
        self.assertFalse(all_valid([1, "2"], is_int))


if __name__ == "__main__":
    unittest.main()
