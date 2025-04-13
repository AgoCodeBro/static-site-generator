from enum import Enum

class TextType(Enum):
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