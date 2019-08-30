#!/usr/bin/env python3

"""
Programming In Python - Lesson 7 Assignment 1: HTML Renderer
Code Poet: Anthony McKeever
Start Date: 08/27/2019
End Date: 
"""

# Knowledge of an HTML Element:
#     Elements have a tag, attributes, and content.
#         The tag denotes the type of the element.
#         Attributes define the propeties of the element.
#         The content is what is display on the page.  This content may be affected by both the tag and the attributes.

#     Basic anatomy:
#         <div class="someclass">some content</div>
    
#     Elements can have child elements as part of their content.  Child elements can inherit CSS propeties of their parent.
#     All items in the HTML DOM (document object model) are elements.
#     Some elements represent a script
#     Some elements are iframes which display another page or HTML document within them.
#     Unique ID attributes are ideal for Selenium attachment.
#         When no ID is present in the child, it may be necessary to daisy chain off the parent to identify the correct child element.
#         XPath and CSS Selectors are notoriously fragile when locating elements with Selenium and can break with even the slightest change in the DOM.


# This is the framework for the base class
class Element(object):

    indent = -1
    
    def __init__(self, content=None, tag="html"):
        self.content = []

        if content is not None:
            self.append(content)

        self.tag = tag
        self.indent += 1
        self.element_attributes = None


    def __str__(self):
        indentation = "  " * self.indent
        return f"\n{indentation}<{self.get_attributes()}>\n{self.get_content()}\n</{self.tag}>"


    def get_content(self):
        output = ""
        for elm in self.content:
            output = output + str(elm)
        return output


    def get_attributes(self):
        attribs = [self.tag]
        if self.element_attributes is not None:
            for k, v in self.element_attributes.items():
                attribs.append("%s=\"%s\"" % (k,v))

        return " ".join(attribs)


    def append(self, new_content):
        self.content.append(new_content)


    def render(self, out_file):
        out_file.write(self.__str__())


class Head(Element):

    def __init__(self, content=None):
        Element.__init__(self, content, "head")


class Title(Element):

    def __init__(self, content=None):
        Element.__init__(self, content, "title")


class Meta(Element):

    def __init__(self, **kwargs):
        Element.__init__(self, None, "meta")
        self.element_attributes = kwargs

    
    def __str__(self):
        return f"<{self.get_attributes()}/>"


class Html(Element):

    def __init__(self, content=None):
        Element.__init__(self, content)

    
    def __str__(self):
        elm_content = Element.__str__(self)
        return f"<!DOCTYPE html>{elm_content}"


class Body(Element):

    def __init__(self, content=None):
        Element.__init__(self, content, "body")


class P(Element):

    def __init__(self, content=None, **kwargs):
        Element.__init__(self, content, "p")
        self.element_attributes = kwargs


class Hr(Element):

    def __init__(self):
        Element.__init__(self, None, "hr")


    def __str__(self):
        return f"\n<{self.tag}/>\n"


class A(Element):

    def __init__(self, href, content):
        Element.__init__(self, content, "a")
        self.element_attributes = {"href": href}

    
    def __str__(self):
        return f"\n<{self.get_attributes()}>{self.get_content()}</{self.tag}>\n"


class Ul(Element):

    def __init__(self, **kwargs):
        Element.__init__(self, None, "ul")
        self.element_attributes = kwargs


class Li(Element):

    def __init__(self, content=None, **kwargs):
        Element.__init__(self, content, "li")
        self.element_attributes = kwargs


class H(Element):
    
    def __init__(self, header_level, content):
        Element.__init__(self, content, f"h{header_level}")