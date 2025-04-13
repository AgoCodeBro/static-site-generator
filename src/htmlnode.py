class htmlnode():
    
    def __init__(self, tag=None, value=None, children=None, props=None):

        self.tag = tag
        self.value = value
        self.children = children
        self.props = props


    def to_html(self):
        raise NotImplementedError()
    

    def props_to_html(self):
        result = ""
        for key in self.props:
            result += f' {key}="{self.props[key]}"'
        return result
    

    def __repr__(self):
        properties = self.props_to_html
        result = f"Tag: {self.tag}\nValue: {self.value}\nChildren: {self.children}\nProperties: {properties}"
        return result
        