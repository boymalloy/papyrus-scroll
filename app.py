from flask import Flask
from flask import render_template, request, redirect, url_for, session
from flask_bootstrap import Bootstrap
from flask import render_template, request
import os
from dotenv import load_dotenv
from pathlib import Path

# Create the Flask app
app = Flask(__name__)

# Load the dev flaskenv
if os.getenv("FLASK_ENV") != "production":
    load_dotenv(".flaskenv")

app.secret_key = "sfklfklfdakl;ad;lk,.cz,.cdslk;dkldkd;lkdkl;dkl;"

# Setup bootstrap
bootstrap = Bootstrap(app)

# Bypass a problematic CDN
app.config["BOOTSTRAP_SERVE_LOCAL"] = True

# from sphinxtensions import DocxExporter
# exporter = DocxExporter()
# exporter.convert_all()

@app.route('/sandbox')
def sandbox_page():
    return render_template('sandbox.html', source_files=source_files)

def list_source_files():
    source_files = []

    for root, dirs, files in os.walk("source/"):
        for file in files:
            file_path = Path(file)
            if file_path.suffix == ".md" and file != "index.md":
                this_file = []
                this_file.append(file)
                title = file_path.stem
                title = title.replace("_", " ")
                title = title.title()
                this_file.append(title)
                source_files.append(this_file)

    return source_files

@app.route('/')
def index():        
    return render_template('index.html', source_files=list_source_files())

@app.route("/edit")
def edit_md():

    file_name = request.args.get('file')
    file_path = "source/" + file_name
    md_text = Path(file_path).read_text(encoding="utf-8")
    return render_template("edit.html", md_text=md_text, file_name=file_name)

@app.route("/save", methods=["GET", "POST"])
def save_md():
    # Get the submissions from the form
    file_name = request.form["file_name"]
    md_text = request.form["md_text"]

    md_path = "source/" + file_name

    with open(md_path, 'w') as file:
        file.write(md_text)

    redirect_url = "/edit?file=" + file_name

    return redirect(redirect_url)