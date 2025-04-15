import unittest

from htmlnode import HTMLNode

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



