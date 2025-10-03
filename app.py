
from flask import Flask, render_template, send_from_directory
import json, os

app = Flask(__name__)

def load_content():
    data_path = os.path.join(app.root_path, "data", "content.json")
    with open(data_path, "r", encoding="utf-8") as f:
        return json.load(f)

@app.context_processor
def inject_globals():
    content = load_content()
    return dict(site=content.get("site", {}))

@app.route("/")
def index():
    content = load_content()
    return render_template("index.html", content=content)

@app.route("/bio")
def bio():
    content = load_content()
    return render_template("bio.html", content=content)

@app.route("/music")
def music():
    content = load_content()
    return render_template("music.html", content=content)

@app.route("/news")
def news():
    content = load_content()
    return render_template("news.html", content=content)

@app.route("/gallery")
def gallery():
    content = load_content()
    return render_template("gallery.html", content=content)

@app.route("/contact")
def contact():
    content = load_content()
    return render_template("contact.html", content=content)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == "__main__":
    # For local run: python app.py
    app.run(host="0.0.0.0", port=5000, debug=True)
