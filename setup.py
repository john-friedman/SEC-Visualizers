from sec_parsers import Filing, set_headers,download_sec_filing, SEC_10K_Parser

set_headers('john smith','johnsmith@example.com')
html =download_sec_filing('https://www.sec.gov/Archives/edgar/data/1318605/000095017022000796/tsla-20211231.htm')

filing = Filing(html)
filing.parse(add_parsing_id=True)
filing.save_xml('tesla.xml')

from lxml import etree

# Assuming you have an lxml object called 'tree'
html_string = etree.tostring(filing.html, pretty_print=True, method="html")

# Save the HTML to a file
with open("tesla.html", "wb") as file:
    file.write(html_string)
