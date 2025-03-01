import unittest
from main import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_valid_h1(self):
        markdown = "# Hello World\nThis is a test."
        self.assertEqual(extract_title(markdown), "Hello World")

    def test_no_h1(self):
        markdown = "## Not an H1\nThis is a test."
        with self.assertRaises(ValueError):
            extract_title(markdown)

    def test_multiple_h1(self):
        markdown = "# First H1\n# Second H1"
        self.assertEqual(extract_title(markdown), "First H1")

    def test_whitespace(self):
        markdown = "   #   Hello World   \nThis is a test."
        self.assertEqual(extract_title(markdown), "Hello World")

if __name__ == "__main__":
    unittest.main()