from flask import Flask
from flask_bootstrap import Bootstrap
from flask import render_template
import os
from dotenv import load_dotenv
from pathlib import Path

# Create the Flask app
app = Flask(__name__)

# Load the dev flaskenv
if os.getenv("FLASK_ENV") != "production":
    load_dotenv(".flaskenv")

# Setup bootstrap
bootstrap = Bootstrap(app)

# Bypass a problematic CDN
app.config["BOOTSTRAP_SERVE_LOCAL"] = True

# from sphinxtensions import DocxExporter
# exporter = DocxExporter()
# exporter.convert_all()

@app.route('/')
def index():
    return render_template('index.html', payload="Greetings")

@app.route("/edit")
def edit_md():
    md_text = Path("source/core_terms.md").read_text(encoding="utf-8")
    return render_template("edit.html", md_text=md_text)