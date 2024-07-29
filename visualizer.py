# visualizer.py
from flask import Flask, render_template
import webbrowser
import threading
import time
from helper import parse_toc_xml
import xml.etree.ElementTree as ET


def open_browser():
    # Wait a bit for the Flask server to start
    time.sleep(1)
    webbrowser.open('http://127.0.0.1:5000/')

def visualizer(toc_file, content_file):
    app = Flask(__name__)

    @app.route('/')
    def index():
        tree = ET.parse('tesla.xml')
        root = tree.getroot()
        document = root.find('document')
        toc_tree = parse_toc_xml(document)
        with open(content_file, 'r') as f:
            content = f.read()
        return render_template('index.html', toc=toc_tree, content=content)

    # Start the browser in a new thread
    threading.Thread(target=open_browser).start()

    # Run the Flask app
    app.run(debug=True, use_reloader=False)

