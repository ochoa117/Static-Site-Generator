import unittest
from markdown_to_textnode import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links
)
from textnode import TextNode, TextType

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.NORMAL_TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE_TEXT)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.NORMAL_TEXT),
                TextNode("code block", TextType.CODE_TEXT),
                TextNode(" word", TextType.NORMAL_TEXT),
            ]
        )

    def test_delim_bold(self):
        node = TextNode("This is text with a **bold block** word", TextType.NORMAL_TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.NORMAL_TEXT),
                TextNode("bold block", TextType.BOLD_TEXT),
                TextNode(" word", TextType.NORMAL_TEXT),
            ]
        )
    
    def test_delim_bold_multiword(self):
        node = TextNode("This is text with a **bold** word and **another**", TextType.NORMAL_TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.NORMAL_TEXT),
                TextNode("bold", TextType.BOLD_TEXT),
                TextNode(" word and ", TextType.NORMAL_TEXT),
                TextNode("another", TextType.BOLD_TEXT)
            ]
        )
    
    def test_delim_italic(self):
        node = TextNode("This is text with an _italic block_ word", TextType.NORMAL_TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC_TEXT)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with an ", TextType.NORMAL_TEXT),
                TextNode("italic block", TextType.ITALIC_TEXT),
                TextNode(" word", TextType.NORMAL_TEXT),
            ]
        )
    
    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and _italic_", TextType.NORMAL_TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC_TEXT)
        self.assertEqual(
            new_nodes,
            [
                TextNode("bold", TextType.BOLD_TEXT),
                TextNode(" and ", TextType.NORMAL_TEXT),
                TextNode("italic", TextType.ITALIC_TEXT)
            ]
        )

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    
    def test_extract_markdown_multiple_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![image2](https://i.imgur2.com/zjjcJKZ.png)"
        )
        self.assertListEqual(
        [
            ("image", "https://i.imgur.com/zjjcJKZ.png"),
            ("image2", "https://i.imgur2.com/zjjcJKZ.png")
        ],
        matches
    )

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev)"
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev")], matches)
    
    def test_extract_markdown_multiple_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual(
        [
            ("to boot dev", "https://www.boot.dev"),
            ("to youtube", "https://www.youtube.com/@bootdotdev")
        ],
        matches
    )
if __name__ == "__main__":
    unittest.main()