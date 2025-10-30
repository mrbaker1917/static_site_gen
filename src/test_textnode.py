import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("Sample text", TextType.ITALIC, url="http://example.com")
        expected_repr = "TextNode(Sample text, italic, http://example.com)"
        self.assertEqual(repr(node), expected_repr)

    def test_invalid_text_type(self):
        with self.assertRaises(TypeError):
            TextNode("Invalid text type", "not_a_text_type")

    def test_url_optional(self):
        node = TextNode("No URL here", TextType.PLAIN)
        self.assertIsNone(node.url)

    def test_text_type_dif(self):
        node1 = TextNode("Same text", TextType.CODE)
        node2 = TextNode("Same text", TextType.IMAGE)
        self.assertNotEqual(node1, node2)
    


if __name__ == "__main__":
    unittest.main()