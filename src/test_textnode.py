import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)
    
    def test_neq(self):
        node = TextNode("This is a text node", TextType.NORMAL_TEXT)
        node2 = TextNode("This is a text node", TextType.ITALIC_TEXT)
        self.assertNotEqual(node, node2)
    
    def test_url(self):
        node = TextNode("This is a text node", TextType.ITALIC_TEXT, "https://boot.dev")
        self.assertNotEqual(node.url, None)
    
    def test_nurl(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node.url, None)


if __name__ == "__main__":
    unittest.main()