
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    def to_html(self):
        raise NotImplementedError("Subclasses should implement this method")
    
    def props_to_html(self):
        if not self.props:
            return ""
        return " " + " ".join(f'{key}="{value}"' for key, value in self.props.items())
    
    def __repr__(self):
        props = " ".join(f"{key}='{value}'" for key, value in self.props.items())
        children = ", ".join(repr(child) for child in self.children)
        return f"HTMLNode(tag={self.tag}, value={self.value}, children=[{children}], props={{{props}}})"

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag=tag, value=value,  props=props)
        self.tag = tag
        self.value = value
        self.props = props if props is not None else {}
    
    def to_html(self):
        if self.value  is None:
            raise ValueError("LeafNode must have a value to convert to HTML")
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"