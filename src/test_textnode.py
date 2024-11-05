import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):

    def test_eq(self):

        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)

        self.assertEqual(node, node2)


    def test_eq_2(self):

        node = TextNode("testing", TextType.ITALIC, "test")
        node2 = TextNode("testing", TextType.ITALIC, "test")

        self.assertEqual(node, node2)

    
    def test_not_eq(self):

        node = TextNode("testing", TextType.BOLD, "test")
        node2 = TextNode("testing", TextType.ITALIC, "test")

        self.assertNotEqual(node, node2)


    def test_none(self):

        node = TextNode("testing", TextType.ITALIC)
        node2 = TextNode("testing", TextType.ITALIC, "test")

        self.assertNotEqual(node, node2)



if __name__ == "__main__":
    unittest.main()
