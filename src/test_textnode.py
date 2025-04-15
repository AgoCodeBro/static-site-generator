import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        # Test 1
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq1(self):
        # Test 2
        node = TextNode("This is a text node", TextType.BOLD, "test")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)        

    def test_not_eq2(self):
        # Test 3
        node = TextNode("This is a text node!", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_eq3(self):
        # Test 4
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    
    
    def test_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'b')
        self.assertEqual(html_node.value, "This is a text node")


    def test_italics(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'i')
        self.assertEqual(html_node.value, "This is a text node")

    def test_code(self):
        node = TextNode("This is a text node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a text node")

    def test_link(self):
        node = TextNode("This is a text node", TextType.LINK)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is a text node", TextType.IMAGE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "This is a text node")


if __name__ == "__main__":
    unittest.main()