import re

from textnode import TextNode, TextType, text_node_to_html


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        parts = node.text.split(delimiter)
        if len(parts) == 1:
            new_nodes.append(node)
            continue
        elif len(parts) == 2 or parts[-1][-1] == delimiter:
            raise Exception("This is invalid Mardown syntax. Delimiter used odd number of times.")
        else:
            for i, part in enumerate(parts):
                if i % 2 == 0:
                    if part:
                        new_nodes.append(TextNode(part, text_type.TEXT))
                else:
                    if part:
                        new_nodes.append(TextNode(part, text_type))
    return new_nodes

def extract_markdown_images(text):
    pattern = r'!\[([^\]]*)\]\(([^)]+)\)'
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    matches = re.findall(pattern, text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        alt_text_url = extract_markdown_images(node.text)
        parts = node.text.split("!")

    return new_nodes