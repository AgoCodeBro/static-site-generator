import unittest

from inline_markdown import split_nodes_delimiter
from textnode import TextNode, TextType

class TestMarkdown(unittest.TestCase):

    def test_code_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(new_nodes, [TextNode("This is text with a ", TextType.TEXT), TextNode("code block", TextType.CODE), TextNode(" word", TextType.TEXT),])


    def test_bold_delimiter2(self):
        node = TextNode("This is text with a **Bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

        self.assertEqual(new_nodes, [TextNode("This is text with a ", TextType.TEXT), TextNode("Bold", TextType.BOLD), TextNode(" word", TextType.TEXT),])
    
    def test_italic_delimiter(self):
        node = TextNode("This is text with a _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)

        self.assertEqual(new_nodes, [TextNode("This is text with a ", TextType.TEXT), TextNode("italic", TextType.ITALIC), TextNode(" word", TextType.TEXT),])
