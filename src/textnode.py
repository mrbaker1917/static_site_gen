from enum import Enum

class TextType(Enum):
    PLAIN = "plain"
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

