from main import *
import unittest

class MainTest(unittest.TestCase):

    def test_extract_title(self):
        markdown = "# Hello  "
        title = extract_title(markdown)

        self.assertEqual(title, "Hello")

    def test_extract_title_error(self):
        markdown = "Hello"
        self.assertRaises(ValueError, extract_title, markdown)

    def test_extract_title_multiline(self):
        markdown =  """
This is a basic markdown file

has multiple blocks
and lines

- a list
- with items

## Secondary Header

# Hello 

### Another header


this should be good lol
"""
        title = extract_title(markdown)
        self.assertEqual(title, "Hello")

    def test_extract_title_no_whitespace(self):
        markdown = "#Hello"
        title = extract_title(markdown)

        self.assertEqual(title, "Hello")

