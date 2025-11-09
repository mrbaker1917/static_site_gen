from enum import Enum

from htmlnode import HTMLNode, LeafNode, ParentNode

from split_nodes_delimiter import split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes
from textnode import TextNode, TextType, text_node_to_html

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDEREDLIST = "unordered_list"
    ORDEREDLIST = "ordered_list"

def markdown_to_blocks(md):
    lines = md.splitlines()
    blocks = []
    curr = []
    in_code = False

    def flush():
        if not curr:
            return
        block = "\n".join(curr)
        # strip non-code blocks; keep code blocks verbatim
        if not (block.startswith("```") and block.rstrip().endswith("```")):
            block = block.strip()
        blocks.append(block)

    for line in lines:
        if line.strip() == "```":
            if in_code:
                curr.append(line)   # closing fence
                flush()
                curr = []
                in_code = False
            else:
                if curr and not any(curr):  # optional: avoid empty preface
                    curr = []
                if curr:
                    flush()
                    curr = []
                curr.append(line)   # opening fence
                in_code = True
            continue

        if in_code:
            curr.append(line)
        else:
            if line.strip() == "":
                flush()
                curr = []
            else:
                curr.append(line)

    flush()
    return blocks


def block_to_block_type(block):
    lines = block.splitlines()
    # opening fence can be ``` or ```lang
    if lines:
        open_line = lines[0].strip()
        close_line = lines[-1].strip()
        if (open_line.startswith("```") and close_line == "```"):
            return BlockType.CODE

    if block.startswith("#"):
        return BlockType.HEADING
    if block.startswith(">"):
        return BlockType.QUOTE
    if block.startswith("- "):
        return BlockType.UNORDEREDLIST
    dot = block.find(". ")
    if dot != -1 and block[:dot].isdigit():
        return BlockType.ORDEREDLIST
    return BlockType.PARAGRAPH
    
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in blocks:
        if not block.strip():
            continue
        block_type = block_to_block_type(block)
        if block_type == BlockType.PARAGRAPH:
            block_parts = block.split("\n")
            block = " ".join(part.strip() for part in block_parts)
            block = block.replace("  ", " ")
            text_nodes = text_to_textnodes(block)
            html_children = [text_node_to_html(node) for node in text_nodes]
            if html_children:
                node = ParentNode("p", html_children)
            else:
                node = ParentNode("p", [LeafNode(None, "")])
        elif block_type == BlockType.HEADING:
            level = block.count("#", 0, block.find(" "))  # Count leading #
            tag = f"h{level}"
            content = block[level+1:].strip()
            text_nodes = text_to_textnodes(content)
            html_children = [text_node_to_html(node) for node in text_nodes]
            if html_children:
                node = ParentNode(tag, html_children)
            else:
                node = ParentNode(tag, [LeafNode(None, "")])
        elif block_type == BlockType.CODE:
            lines = block.splitlines()
            code_content = "\n".join(lines[1:-1]) + "\n"
            node = ParentNode("pre", [LeafNode("code", code_content)])
        elif block_type == BlockType.QUOTE:
            quote_content = block[1:].strip()
            text_nodes = text_to_textnodes(quote_content)
            html_children = [text_node_to_html(node) for node in text_nodes]
            if html_children:
                node = ParentNode("blockquote", html_children)
            else:
                node = ParentNode("blockquote", [LeafNode(None, "")])
        elif block_type == BlockType.UNORDEREDLIST:
            items = [item[2:].strip() for item in block.split("\n")]
            li_nodes = []
            for item in items:
                text_nodes = text_to_textnodes(item)
                html_children = [text_node_to_html(node) for node in text_nodes]
                if html_children:
                    li_nodes.append(ParentNode("li", html_children))
                else:
                    li_nodes.append(ParentNode("li", [LeafNode(None, "")]))
            node = ParentNode("ul", li_nodes)
        elif block_type == BlockType.ORDEREDLIST:
            items = [item[item.find(". ")+2:].strip() for item in block.split("\n")]
            li_nodes = []
            for item in items:
                text_nodes = text_to_textnodes(item)
                html_children = [text_node_to_html(node) for node in text_nodes]
                if html_children:
                    li_nodes.append(ParentNode("li", html_children))
                else:
                    li_nodes.append(ParentNode("li", [LeafNode(None, "")]))
            node = ParentNode("ol", li_nodes)
        html_nodes.append(node)
    return ParentNode("div", html_nodes)