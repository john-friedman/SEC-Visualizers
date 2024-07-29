# visualizer.py
from flask import Flask, render_template
import webbrowser
import threading
import time
from helper import parse_toc_xml



def open_browser():
    # Wait a bit for the Flask server to start
    time.sleep(1)
    webbrowser.open('http://127.0.0.1:5000/')

def visualizer(toc_file, content_file):
    app = Flask(__name__)

    @app.route('/')
    def index():
        toc = parse_toc_xml(toc_file)
        with open(content_file, 'r') as f:
            content = f.read()
        return render_template('index.html', toc=toc, content=content)

    # Start the browser in a new thread
    threading.Thread(target=open_browser).start()

    # Run the Flask app
    app.run(debug=True, use_reloader=False)

if __name__ == '__main__':
    visualizer('tesla.xml', 'tesla.html')

# The HTML template remains the same as in the previous version