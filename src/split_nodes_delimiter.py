import re

from textnode import TextNode, TextType, text_node_to_html


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        parts = node.text.split(delimiter)
        if len(parts) == 1:
            new_nodes.append(node)
            continue
        elif len(parts) % 2 == 0:
            raise Exception("This is invalid Mardown syntax. Delimiter used odd number of times.")
        else:
            for i, part in enumerate(parts):
                if i % 2 == 0:
                    if part:
                        new_nodes.append(TextNode(part, TextType.TEXT))
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
        if "!" not in node.text:
            new_nodes.append(node)
            continue
        alt_text_url = extract_markdown_images(node.text)
        parts = node.text.split("!")
        for part in parts:
            if not part:
                continue          
            remaining_part = part
            while alt_text_url and f"[{alt_text_url[0][0]}]({alt_text_url[0][1]})" in remaining_part:
                image_markdown = f"[{alt_text_url[0][0]}]({alt_text_url[0][1]})"
                before, after = remaining_part.split(image_markdown, 1)
                if before:
                    new_nodes.append(TextNode(before, TextType.TEXT))
                new_nodes.append(TextNode(alt_text_url[0][0], TextType.IMAGE, url=alt_text_url[0][1]))
                alt_text_url.pop(0)
                remaining_part = after
            
            if remaining_part:
                new_nodes.append(TextNode(remaining_part, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if "[" not in node.text:
            new_nodes.append(node)
            continue
        link_text_url = extract_markdown_links(node.text)
        parts = node.text.split("[")
        for part in parts:
            if not part:
                continue          
            remaining_part = part
            while link_text_url and f"]({link_text_url[0][1]})" in remaining_part:
                link_markdown = f"]({link_text_url[0][1]})"
                before, after = remaining_part.split(link_markdown, 1)
                link_text = before.split("]")[0]
                if "]" in before:
                    text_before_link = before[:before.index("]")]
                    if text_before_link:
                        new_nodes.append(TextNode(text_before_link, TextType.TEXT))
                new_nodes.append(TextNode(link_text, TextType.LINK, url=link_text_url[0][1]))
                link_text_url.pop(0)
                remaining_part = after
            
            if remaining_part:
                new_nodes.append(TextNode(remaining_part, TextType.TEXT))
    return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes