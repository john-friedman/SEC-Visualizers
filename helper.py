import xml.etree.ElementTree as ET

# fix to make nested
def parse_toc_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    document = root.find('document')
    toc = []
    for item in document.iter():
        toc.append({
            'title': item.attrib.get('title'),
            'parsing_id': item.attrib.get('parsing_id'),
        })
    return toc