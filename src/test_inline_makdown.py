import unittest

from inline_markdown import *
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


    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images2(self):
        matches = extract_markdown_images(
            "This is text with an [image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("link", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links2(self):
        matches = extract_markdown_links(
            "This is text with an ![link](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([], matches)

    def test_split_images(self):
        markdown = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)"
        node = TextNode(markdown, TextType.TEXT)

        new_nodes = split_nodes_image([node])

        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        markdown = "This is text with a [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)"
        node = TextNode(markdown, TextType.TEXT)
        
        new_nodes = split_nodes_link([node])

        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    
    def test_no_link(self):
        markdown = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)"
        node = TextNode(markdown, TextType.TEXT)

        new_nodes = split_nodes_link([node])

        self.assertEqual([TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        ),], new_nodes)

    def test_no_image(self):
        markdown = "This is text with an [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)"
        node = TextNode(markdown, TextType.TEXT)

        new_nodes = split_nodes_image([node])

        self.assertEqual([TextNode(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        ),], new_nodes)

    def test_start_with_image(self):
        markdown = "![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png) for this test"
        node = TextNode(markdown, TextType.TEXT)

        new_nodes = split_nodes_image([node])

        self.assertEqual([TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"), 
                          TextNode(" and another ", TextType.TEXT), 
                          TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
                          TextNode(" for this test", TextType.TEXT)],
                          new_nodes)
        
    def test_start_with_link(self):
        markdown = "[link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png) for this test"
        node = TextNode(markdown, TextType.TEXT)

        new_nodes = split_nodes_link([node])

        self.assertEqual([TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"), 
                          TextNode(" and another ", TextType.TEXT), 
                          TextNode("second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"),
                          TextNode(" for this test", TextType.TEXT)],
                          new_nodes)
        
    def test_double_image(self):
        markdown = "testing two ![image one](https://blahlbah.png)![image two](lol.png) back to back" 
        node = TextNode(markdown, TextType.TEXT)

        new_nodes = split_nodes_image([node])

        self.assertEqual([TextNode("testing two ", TextType.TEXT),
                          TextNode("image one", TextType.IMAGE, "https://blahlbah.png"),
                          TextNode("image two", TextType.IMAGE, "lol.png"),
                          TextNode(" back to back", TextType.TEXT)],
                          new_nodes)
        
    def test_double_link(self):
        markdown = "testing two [link one](https://blahlbah.png)[link two](lol.png) back to back" 
        node = TextNode(markdown, TextType.TEXT)

        new_nodes = split_nodes_link([node])

        self.assertEqual([TextNode("testing two ", TextType.TEXT),
                          TextNode("link one", TextType.LINK, "https://blahlbah.png"),
                          TextNode("link two", TextType.LINK, "lol.png"),
                          TextNode(" back to back", TextType.TEXT)],
                          new_nodes)

    def test_solo_image(self):
        markdown = "![image](https://i.imgur.com/zjjcJKZ.png)"
        node = TextNode(markdown, TextType.TEXT)

        new_nodes = split_nodes_image([node])

        self.assertEqual([TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),], new_nodes)

    def test_solo_link(self):
        markdown = "[link](https://i.imgur.com/zjjcJKZ.png)"
        node = TextNode(markdown, TextType.TEXT)

        new_nodes = split_nodes_link([node])

        self.assertEqual([TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),], new_nodes)

