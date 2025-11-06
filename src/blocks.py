from enum import Enum

from htmlnode import HTMLNode, LeafNode, ParentNode

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDEREDLIST = "unordered_list"
    ORDEREDLIST = "ordered_list"

def markdown_to_blocks(markdown):
    unstripped_blocks = markdown.split("\n\n")
    blocks = [block.strip() for block in unstripped_blocks]
    return blocks


def block_to_block_type(block):
    if block.startswith("#"):
        return BlockType.HEADING
    elif block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    elif block.startswith(">"):
        return BlockType.QUOTE
    elif block.startswith("- "):
        return BlockType.UNORDEREDLIST
    elif block[:block.find(". ")].isdigit():
        return BlockType.ORDEREDLIST
    else:
        return BlockType.PARAGRAPH