import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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
    
    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"}
            )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})"
            )
    
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
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node2.to_html(), '<a href="https://www.google.com">Click me!</a>')
    
    def test_leaf_to_html_no_tag(self):
        node4 = LeafNode(None, "Hello, world!")
        self.assertEqual(node4.to_html(), "Hello, world!")
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_with_no_children(self):
        node = ParentNode("div", [])
        self.assertEqual(
            node.to_html(),
            "<div></div>"
        )

    def test_to_html_with_multiple_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "Italic text"),
                LeafNode(None, "Normal text")
            ]
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>Italic text</i>Normal text</p>"
        )
    
    def test_to_html_with_multiple_grandchildren(self):
        node = ParentNode(
            "p",
            [
                ParentNode("div", [LeafNode("b", "Bold text"), LeafNode(None, "Normal text")]),
                LeafNode("i", "Italic text"),
            ]
        )
        self.assertEqual(
            node.to_html(),
            "<p><div><b>Bold text</b>Normal text</div><i>Italic text</i></p>"
        )
    
    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "Italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>Italic text</i>Normal text</h2>",
        )

if __name__ == "__main__":
    unittest.main()