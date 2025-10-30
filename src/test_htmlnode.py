import unittest

from htmlnode import HTMLNode


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

if __name__ == "__main__":
    unittest.main()