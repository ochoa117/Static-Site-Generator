import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        props_html = ' href="https://www.google.com" target="_blank"'
        node = HTMLNode(None, None, None, props)
        self.assertEqual(node.props_to_html(), props_html)
    
    def test_isNone(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)
    
    def test_isNotNone(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode("p", "This is paragraph text", [], props)
        self.assertIsNotNone(node.tag)
        self.assertIsNotNone(node.value)
        self.assertIsNotNone(node.children)
        self.assertIsNotNone(node.props)