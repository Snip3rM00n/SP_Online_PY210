#!/usr/bin/env python3

"""
Programming In Python - Lesson 7 Assignment 1: HTML Renderer
Code Poet: Anthony McKeever
Start Date: 08/27/2019
End Date: 08/30/2019

This version meets the requirement of properly rendering an HTML document.
However it does not meet the class requirements:
    * Using the renderer to indent as opposed to self.__str__
    * Self closing elements do not use their own self closing method/class
    * 
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

    indent = 1
    
    def __init__(self, content=None, tag="html", **kwargs):
        self.content = []

        if content is not None:
            self.append(content)

        self.tag = tag
        self.element_attributes = kwargs


    def __str__(self):
        indentation = self.get_indent()
        inner_html, close_indent = self.get_content(indentation)
        return f"<{self.get_attributes()}>{inner_html}\n{close_indent}</{self.tag}>"


    def get_indent(self, c=""):
        return c + ("    " * self.indent)


    def get_content(self, c="", new_lines=True):
        output = ""
        total_indent = self.get_indent(c)
        nl = "\n" if new_lines else ""

        for elm in self.content:
            elm_str = str(elm)
            
            if elm_str[0] != "<":
                output = f"{output}{nl}{total_indent}{self.get_indent()}{elm_str}"
            
            else:
                output = f"{output}{nl}{total_indent}{elm_str}"

        return output, c


    def get_attributes(self):
        attribs = [self.tag]
        if self.element_attributes is not None:
            for k, v in self.element_attributes.items():
                attribs.append("%s=\"%s\"" % (k,v))

        return " ".join(attribs)


    def append(self, new_content):
        self.content.append(new_content)


    def render(self, out_file, ind=""):
        out_file.write(f"{ind}{self.__str__()}")


class Head(Element):

    def __init__(self, content=None):
        Element.__init__(self, content, "head")


class Title(Element):

    def __init__(self, content=None):
        Element.__init__(self, content, "title")

    
    def __str__(self):
        inner_text, __ = self.get_content(new_lines=False)
        return f"<{self.get_attributes()}>{inner_text.strip()}</{self.tag}>"


class Meta(Element):

    def __init__(self, **kwargs):
        Element.__init__(self, None, "meta", **kwargs)

    
    def __str__(self):
        return f"<{self.get_attributes()} />"


class Html(Element):

    def __init__(self, content=None):
        Element.__init__(self, content, "html")


    def __str__(self):
        elm_content, __ = self.get_content()
        return f"<!DOCTYPE html>\n<html>{elm_content}\n</html>"


class Body(Element):

    def __init__(self, content=None):
        Element.__init__(self, content, "body")


class P(Element):

    def __init__(self, content=None, **kwargs):
        Element.__init__(self, content, "p", **kwargs)


    def get_content(self, c="", new_lines=True):
        inner_html = ""
        indent = self.get_indent(c)

        for inner in self.content:
            inner_content = str(inner)
            inner_html = inner_html + "\n" + indent + self.get_indent() + inner_content

        return f"{inner_html}", indent

class Hr(Element):

    def __init__(self, **kwargs):
        Element.__init__(self, None, "hr", **kwargs)


    def __str__(self):
        return f"<{self.get_attributes()} />"


class A(Element):

    def __init__(self, href, content, **kwargs):
        Element.__init__(self, content, "a")
        self.element_attributes = {"href": href}
        self.element_attributes.update(kwargs)

    
    def __str__(self):
        inner_text, __ = self.get_content(new_lines=False)
        return f"<{self.get_attributes()}>{inner_text.strip()}</{self.tag}>"


class Ul(Element):

    def __init__(self, **kwargs):
        Element.__init__(self, None, "ul")
        self.element_attributes = kwargs


    def get_content(self, c="", new_lines=True):
        inner_html = ""
        indent = self.get_indent(c)

        for inner in self.content:
            inner_content = str(inner)
            inner_html = inner_html + "\n" + indent + self.get_indent() + inner_content

        return f"{inner_html}", indent
        

class Li(Element):

    def __init__(self, content=None, **kwargs):
        Element.__init__(self, content, "li", **kwargs)


    def get_content(self, c="", new_lines=True):
        inner_html = ""
        indent = self.get_indent(c) * 2

        for inner in self.content:
            inner_html = inner_html + "\n" + indent + str(inner)

        return f"{indent}{inner_html}", indent[:-len(self.get_indent())]


class H(Element):
    
    def __init__(self, header_level, content):
        Element.__init__(self, content, f"h{header_level}")

        
    def __str__(self):
        inner_text, __ = self.get_content(new_lines=False)
        return f"<{self.get_attributes()}>{inner_text.strip()}</{self.tag}>"
