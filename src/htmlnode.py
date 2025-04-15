class HTMLNode():
    
    def __init__(self, tag=None, value=None, children=None, props=None):

        self.tag = tag
        self.value = value
        self.children = children
        self.props = props


    def to_html(self):
        raise NotImplementedError()
    

    def props_to_html(self):
        result = ""
        if self.props is None:
            return result
        
        else:
            for key in self.props:
                result += f' {key}="{self.props[key]}"'
            return result
    

    def __repr__(self):
        properties = self.props_to_html
        result = f"Tag: {self.tag}\nValue: {self.value}\nChildren: {self.children}\nProperties: {properties}"
        return result
        

class LeafNode(HTMLNode):

    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        
        elif self.tag is None:
            return self.value
        
        else:
            return f"<{self.tag+self.props_to_html()}>{self.value}</{self.tag}>"