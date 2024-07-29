# visualizer.py
from flask import Flask, render_template
import webbrowser
import threading
import time
from sec_visualizers.helper import parse_toc_xml
import xml.etree.ElementTree as ET
from pathlib import Path
import pkg_resources

def open_browser():
    # Wait a bit for the Flask server to start
    time.sleep(1)
    webbrowser.open('http://127.0.0.1:5000/')

    
app = Flask(__name__, 
            template_folder=pkg_resources.resource_filename('sec_visualizers', 'templates'))

def visualizer(root, html):
    @app.route('/')
    def index():
        document = root.find('document')
        toc_tree = parse_toc_xml(document)
        return render_template('index.html', toc=toc_tree, content=html)

    # Start the browser in a new thread
    threading.Thread(target=open_browser).start()

    # Run the Flask app
    app.run(debug=True, use_reloader=False)