from textnode import TextNode, TextType
        
def main():
    obj = TextNode("This is a text node", TextType.BOLD_TEXT, "https://www.boot.dev")
    obj_str = obj.__repr__()
    print(obj_str)

main()