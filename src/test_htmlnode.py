# import unittest

# from htmlnode import HTMLNode, LeafNode, ParentNode
# from textnode import TextNode, TextType, text_node_to_html


# class TestHTMLNode(unittest.TestCase):
#     def test_repr(self):
#         node = HTMLNode("div", "Hello, World!", props={"class": "greeting"})
#         expected_repr = "HTMLNode(tag=div, value=Hello, World!, children=[], props={class='greeting'})"
#         self.assertEqual(repr(node), expected_repr)

#     def test_props_to_html(self):
#         node = HTMLNode("img", None, props={"src": "image.png", "alt": "An image"})
#         self.assertEqual(node.props_to_html(), ' src="image.png" alt="An image"')
    
#     def test_props_to_html_empty(self):
#         node = HTMLNode("p", "No props here")
#         self.assertEqual(node.props_to_html(), "")

#         #tests for LeafNode:
#     def test_leaf_to_html_p(self):
#         node = LeafNode("p", "Hello, world!")
#         self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

#     def test_leaf_to_html_no_tag(self):
#         node = LeafNode(None, "Just some text")
#         self.assertEqual(node.to_html(), "Just some text")

#     def test_leaf_to_html_with_props(self):
#         node = LeafNode("a", "Click here", props={"href": "http://example.com", "target": "_blank"})
#         self.assertEqual(node.to_html(), '<a href="http://example.com" target="_blank">Click here</a>')

#     def test_to_html_with_children(self):
#         child_node = LeafNode("span", "child")
#         parent_node = ParentNode("div", [child_node])
#         self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

#     def test_to_html_with_grandchildren(self):
#         grandchild_node = LeafNode("b", "grandchild")
#         child_node = ParentNode("span", [grandchild_node])
#         parent_node = ParentNode("div", [child_node])
#         self.assertEqual(
#             parent_node.to_html(),
#             "<div><span><b>grandchild</b></span></div>",
#         )
#     def test_to_html_parent_noKids(self):
#         parent_node = ParentNode("div", None)
#         with self.assertRaises(ValueError):
#             parent_node.to_html()

#     def test_to_html_parent_inside_parent(self):
#         child_node = ParentNode("p", None)
#         parent_node = ParentNode("div", [child_node])
#         with self.assertRaises(ValueError):
#             parent_node.to_html()

#     def test_to_html_many_kids(self):
#         child1 = LeafNode("li", "Item 1")
#         child2 = LeafNode("li", "Item 2")
#         child3 = LeafNode("li", "Item 3")
#         parent_node = ParentNode("ul", [child1, child2, child3])
#         self.assertEqual(
#             parent_node.to_html(),
#             "<ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul>",
#         )
    
#     def test_text(self):
#         node = TextNode("This is a text node", TextType.TEXT)
#         html_node = text_node_to_html(node)
#         self.assertEqual(html_node.tag, None)
#         self.assertEqual(html_node.value, "This is a text node")

#     def test_bold(self):
#         node = TextNode("Bold text", TextType.BOLD)
#         html = text_node_to_html(node)
#         self.assertEqual(html, "<strong>Bold text</strong>")
    
#     def test_link(self):
#         node = TextNode("Example", TextType.LINK, url="http://example.com")
#         html = text_node_to_html(node)
#         self.assertEqual(html, '<a href="http://example.com">Example</a>')

#     def test_image(self):
#         node = TextNode("An image", TextType.IMAGE, url="http://example.com/image.png")
#         html = text_node_to_html(node)
#         self.assertEqual(html, '<img src="http://example.com/image.png" alt="An image"/>')

#     def test_code(self):
#         node = TextNode("print('Hello, World!')", TextType.CODE)
#         html = text_node_to_html(node)
#         self.assertEqual(html, "<code>print('Hello, World!')</code>")

#     def test_italic(self):
#         node = TextNode("Italic text", TextType.ITALIC)
#         html = text_node_to_html(node)
#         self.assertEqual(html, "<em>Italic text</em>")  

        
# if __name__ == "__main__":
#     unittest.main()