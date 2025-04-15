import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):

    def test1(self):
        node1 = HTMLNode("a", "This is a test", None, {"href": "https://www.google.com", "target": "_blank",})
        
        self.assertEqual(node1.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test2(self):
        node1 = HTMLNode("a", "This is a test", None, {"href": "https://www.google.com", "target": "_blank",})
        
        # Veryfying space at the start
        self.assertNotEqual(node1.props_to_html(), 'href="https://www.google.com" target="_blank"')

    def test3(self):
        node1 = HTMLNode("a", "This is a test", "test", {"href": "https://www.google.com", "target": "_blank", "value": "0"})
        
        self.assertEqual(node1.props_to_html(), ' href="https://www.google.com" target="_blank" value="0"')

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leat_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')
        



