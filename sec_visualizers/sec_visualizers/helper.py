import xml.etree.ElementTree as ET

class Node:
    def __init__(self, name, content=None):
        self.name = name
        self.content = content
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def __repr__(self):
        return f"Node({self.name}, children: {len(self.children)})"

def parse_toc_xml(element):
    node = Node(element.attrib['title'])
    node.parsing_id = element.attrib.get('parsing_id')
    for child in element:
        node.add_child(parse_toc_xml(child))
    return node

# fix to make nested
# def parse_toc_xml(xml_file):
#     tree = ET.parse(xml_file)
#     root = tree.getroot()
#     document = root.find('document')
#     toc = []
#     for item in document.iter():
#         toc.append({
#             'title': item.attrib.get('title'),
#             'parsing_id': item.attrib.get('parsing_id'),
#         })
#     return toc