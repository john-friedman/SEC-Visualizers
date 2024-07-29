from sec_visualizers import visualizer
from sec_downloaders import SEC_Downloader
from sec_parsers import Filing
from lxml import etree
downloader = SEC_Downloader()
downloader.set_headers("John Doe", "johndoe@example.com")
url = 'https://www.sec.gov/Archives/edgar/data/1318605/000095017022000796/tsla-20211231.htm'
download = downloader.download(url)
filing = Filing(download)

filing.parse(add_parsing_id=True)

html_string = etree.tostring(filing.html, pretty_print=True, method="html")

visualizer(filing.xml, html_string.decode('utf-8'))