

class HTMLNode:

    def __init__(self, tag=None, value=None, children=None, props=None):
        
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props




    def to_html(self):

        raise NotImplementedError


    def props_to_html(self):

        result = ""
        if self.props is None:
            raise Exception("Props is empty")

        for attribute in self.props:
            result += f" {attribute}=\"{self.props[attribute]}\""

        return result

    
    def __repr__(self):

        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"