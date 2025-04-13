from textnode import TextNode, TextType

def main():
    node = TextNode("testing", TextType.BOLD, "www.testlol.com")
    print(node)

if __name__ == "__main__":
    main()