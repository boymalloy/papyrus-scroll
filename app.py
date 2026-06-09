from flask import Flask
from flask_bootstrap import Bootstrap
from flask import render_template
import os
import pypandoc
from dotenv import load_dotenv
from pathlib import Path
import subprocess

# Create the Flask app
app = Flask(__name__)

# Load the dev flaskenv
if os.getenv("FLASK_ENV") != "production":
    load_dotenv(".flaskenv")

# Setup bootstrap
bootstrap = Bootstrap(app)

# Bypass a problematic CDN
app.config["BOOTSTRAP_SERVE_LOCAL"] = True

# Run sphinx to create html versions of every md file
def sphinx_make_html():
    result = subprocess.run(
        ["make", "html"],
        capture_output=True,
        text=True
    )

    return result.returncode

# Convert an html file to a docx file, including updating the links within the files
def html_docx_convert(html_file):
    html_path = Path(html_file)
    slug = html_path.stem

    with open(html_file, 'r') as file:
        
        # find .html links within the html file and replace them with .docx links
        search_text = ".html"
        replace_text = ".docx"
        data = file.read()
        data = data.replace(search_text, replace_text)

    # Write the updated file as a temp file
    with open('build/html/temp.html', 'x') as file:
        file.write(data)
    
    # Convert the temp file to a docx file using pandoc
    pypandoc.convert_file("build/html/temp.html", "docx", outputfile="docs/" + slug + ".docx")

    # return a data version of the updated html file for testing
    return data

def convert_all():
    
    # Make fresh versions of all the html files
    sphinx_make_html()
    
    # Get all the files in the html folder
    all_files = [
        os.path.join(root, file)
        for root, dirs, files in os.walk("build/html")
        for file in files
    ]

    # Loop through all the files
    for file in all_files:
        file_path = Path(file)
        # where the file is an html file
        if file_path.suffix == ".html":
            # ... convert it to a docx and update the links within it
            html_docx_convert(file)
            # Remove the temp html file that needs to be created each time 
            os.remove("build/html/temp.html")

# convert_all()

@app.route('/')
def index():
    return render_template('index.html', payload="Nothing to see yet")