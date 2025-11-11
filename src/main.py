from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from blocks import markdown_to_blocks, block_to_block_type, markdown_to_html_node, BlockType
from split_nodes_delimiter import split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes
from textnode import text_node_to_html
import os
import shutil

def copy_directory(src, dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)
    os.makedirs(dest, exist_ok=True)
    
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dest_path = os.path.join(dest, item)
        
        if os.path.isdir(src_path):
            copy_directory(src_path, dest_path)
        else:
            shutil.copy2(src_path, dest_path)

def extract_title(markdown):
    lines = markdown.splitlines()
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    raise Exception("No title found in markdown")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    md = ""
    with open(from_path, 'r', encoding='utf-8') as f:
        md = f.read()
    
    template = ""
    with open(template_path, 'r', encoding='utf-8') as f:
        template = f.read()

    html_string = markdown_to_html_node(md).to_html()

    title = extract_title(md)
    final_html = template.replace("{{ Title }}", title).replace("{{ Content }}", html_string)
    print(f"Final HTML: {final_html}")
    
    index_path = os.path.join(dest_path, "index.html")
    # Ensure the destination directory exists
    os.makedirs(os.path.dirname(index_path), exist_ok=True)
    print(f"Writing generated page to {index_path}")
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(final_html)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for item in os.listdir(dir_path_content):
        item_path = os.path.join(dir_path_content, item)
            
        if os.path.isfile(item_path) and item.endswith('.md'):
            # Generate page for markdown file
            generate_page(item_path, template_path, dest_dir_path)
        elif os.path.isdir(item_path):
            # Recursively process subdirectories
            dest_subdir = os.path.join(dest_dir_path, item)
            generate_pages_recursive(item_path, template_path, dest_subdir)


def main():

    generate_pages_recursive("content", "template.html", "static")
    source_dir = "static"
    destination_dir = "public"
    copy_directory(source_dir, destination_dir)
    print(f"Copied contents from {source_dir} to {destination_dir}")
main()