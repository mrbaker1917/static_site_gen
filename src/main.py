from textnode import TextNode, TextType

def main():
    node1 = TextNode(text="this is a paragraph", text_type=TextType.LINK, url="https://mrbaker1917.com")
    print(node1)
main()