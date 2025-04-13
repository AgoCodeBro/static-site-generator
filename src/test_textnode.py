import unittest

from textnode import TextNode, TextType


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


if __name__ == "__main__":
    unittest.main()