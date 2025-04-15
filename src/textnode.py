from htmlnode import HTMLNode, ParentNode, LeafNode
from enum import Enum

class TextType(Enum):
    TEXT = "Text"
    BOLD = "Bold"
    ITALIC = "Italics"
    CODE = "Code"
    LINK = "Link"
    IMAGE = "Image"


class TextNode():

    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url


    def __eq__(self, value):
        if self.text != value.text:
            return False
        elif self.text_type != value.text_type:
            return False
        elif self.url != value.url:
            return False
        else:
            return True
        
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    

def text_node_to_html_node(text_node):
    if  text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)

    elif text_node.text_type == TextType.BOLD:
        return LeafNode('b', text_node.text)
    
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode('i', text_node.text)
    
    elif text_node.text_type == TextType.CODE:
        return LeafNode('code', text_node.text)
    
    elif text_node.text_type == TextType.LINK:
        return LeafNode('a', text_node.text)
    
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode('img', text_node.text)
    
    else:
        raise Exception("Invalid text type")