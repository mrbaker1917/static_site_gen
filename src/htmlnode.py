
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
