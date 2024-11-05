import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_repr(self):
        node = HTMLNode("p", "testing", "test", "test")

        self.assertEqual(repr(node), "HTMLNode(p, testing, test, test)")


    def test_props_to_html(self):

        dict = {"href": "https://www.google.com", "target": "_blank"}
        list = ["test", "testin"]

        node = HTMLNode("p", "Test node", list, dict)

        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')


    def test_to_html(self):

        with self.assertRaises(NotImplementedError):
            node = HTMLNode()
            node.to_html()


