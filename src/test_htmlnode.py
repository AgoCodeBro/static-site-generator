import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_child_missing_children(self):
        child_node = ParentNode("span", None)
        parent_node = ParentNode("div", [child_node])
        self.assertRaises(ValueError, parent_node.to_html)



