import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("div", "Hello, World!", props={"class": "greeting"})
        expected_repr = "HTMLNode(tag=div, value=Hello, World!, children=[], props={class='greeting'})"
        self.assertEqual(repr(node), expected_repr)

    def test_props_to_html(self):
        node = HTMLNode("img", None, props={"src": "image.png", "alt": "An image"})
        self.assertEqual(node.props_to_html(), ' src="image.png" alt="An image"')
    
    def test_props_to_html_empty(self):
        node = HTMLNode("p", "No props here")
        self.assertEqual(node.props_to_html(), "")

        #tests for LeafNode:
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Just some text")
        self.assertEqual(node.to_html(), "Just some text")

    def test_leaf_to_html_with_props(self):
        node = LeafNode("a", "Click here", props={"href": "http://example.com", "target": "_blank"})
        self.assertEqual(node.to_html(), '<a href="http://example.com" target="_blank">Click here</a>')

if __name__ == "__main__":
    unittest.main()