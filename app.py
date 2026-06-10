from flask import Flask
from flask_bootstrap import Bootstrap
from flask import render_template
import os
from dotenv import load_dotenv
from sphinxtensions import DocxExporter

# Create the Flask app
app = Flask(__name__)

# Load the dev flaskenv
if os.getenv("FLASK_ENV") != "production":
    load_dotenv(".flaskenv")

# Setup bootstrap
bootstrap = Bootstrap(app)

# Bypass a problematic CDN
app.config["BOOTSTRAP_SERVE_LOCAL"] = True

exporter = DocxExporter()
exporter.convert_all()

@app.route('/')
def index():
    return render_template('index.html', payload="Nothing to see yet")