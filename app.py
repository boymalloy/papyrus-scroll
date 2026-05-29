from flask import Flask
from flask_bootstrap import Bootstrap
from flask import render_template, request, redirect, url_for, session

# Create the Flask app
app = Flask(__name__)

app.config["BOOTSTRAP_SERVE_LOCAL"] = True

# Build extensions
bootstrap = Bootstrap(app)

# Route: Home page
@app.route('/')
def index():
    return render_template('index.html')