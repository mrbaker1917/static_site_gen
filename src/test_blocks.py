import unittest

from blocks import markdown_to_blocks, block_to_block_type, BlockType

class TestBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
            md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
        """
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                    blocks,
                    [
                        "This is **bolded** paragraph",
                        "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                        "- This is a list\n- with items",
                    ],
            )

    def test_markdown_to_blocks_single_paragraph(self):
            md = "This is a single paragraph without any double newlines."
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is a single paragraph without any double newlines.",
                ],
            )
    def test_markdown_to_blocks_leading_trailing_newlines(self):
            md = """
    This is a paragraph with leading and trailing newlines.   
    """
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is a paragraph with leading and trailing newlines.",
                ],
            )

    def test_block_to_block_type(self):
            self.assertEqual(block_to_block_type("# Heading 1"), BlockType.HEADING)
            self.assertEqual(
                block_to_block_type("```python\nprint('Hello, World!')\n```"),
                BlockType.CODE,
            )
            self.assertEqual(block_to_block_type("> This is a quote"), BlockType.QUOTE)
            self.assertEqual(block_to_block_type("- Item 1"), BlockType.UNORDEREDLIST)
            self.assertEqual(block_to_block_type("1. First item"), BlockType.ORDEREDLIST)
            self.assertEqual(
                block_to_block_type("This is a regular paragraph."), BlockType.PARAGRAPH
            )


if __name__ == "__main__":
    unittest.main()