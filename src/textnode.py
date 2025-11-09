from enum import Enum

from htmlnode import HTMLNode, LeafNode, ParentNode

class TextType(Enum):
    TEXT = "text"
    LINK = "link"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    IMAGE = "image"

class TextNode:

    def __init__(self, text, text_type, url=None):
        self.text = text
        self.url = url
        if not isinstance(text_type, TextType):
            raise TypeError("text_type must be an instance of TextType Enum")
        self.text_type = text_type

    def __eq__(self, other):
        return (
            self.text == other.text and
            self.text_type == other.text_type and
            self.url == other.url
        )
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html(node):
    if node.text_type == TextType.TEXT:
        return LeafNode(None, node.text)
    elif node.text_type == TextType.BOLD:
        return LeafNode("b", node.text)
    elif node.text_type == TextType.ITALIC:
        return LeafNode("i", node.text)
    elif node.text_type == TextType.CODE:
        return LeafNode("code", node.text)
    elif node.text_type == TextType.LINK:
        if node.url is None:
            raise ValueError("URL must be provided for link text nodes")
        return LeafNode("a", node.text, {"href": node.url})
    elif node.text_type == TextType.IMAGE:
        if node.url is None:
            raise ValueError("URL must be provided for image text nodes")
        return LeafNode("img", "", {"src": node.url, "alt": node.text})
    else:
        raise ValueError("Unsupported text type")
    