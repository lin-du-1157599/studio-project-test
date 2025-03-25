# This script runs automatically when our `app` module is first loaded,
# and handles all the setup for our Flask app.
from flask import Flask, redirect, url_for
import os

app = Flask(__name__)

# Configure upload folder for event images
from app.config import constants
app.config[constants.IMAGE_UPLOAD_FOLDER] = os.path.join(app.root_path, 'static', 'uploads')
os.makedirs(app.config[constants.IMAGE_UPLOAD_FOLDER], exist_ok=True)

# Add multiple template search paths to Jinja2 template loader.
# This allows Flask to locate templates stored in different subdirectories under 'templates'.
app.jinja_loader.searchpath.append(os.path.join(app.root_path, 'templates', 'base'))
app.jinja_loader.searchpath.append(os.path.join(app.root_path, 'templates', 'auth'))
app.jinja_loader.searchpath.append(os.path.join(app.root_path, 'templates', 'home'))
app.jinja_loader.searchpath.append(os.path.join(app.root_path, 'templates', 'user'))
app.jinja_loader.searchpath.append(os.path.join(app.root_path, 'templates', 'event'))

# Set the "secret key" that our app will use to sign session cookies.
app.secret_key = 'Example Secret Key (CHANGE THIS TO YOUR OWN SECRET KEY!)'

# Set up database connection.
from app.db.connect import dbuser, dbpass, dbhost, dbname
from app.db.db import init_db
init_db(app, dbuser, dbpass, dbhost, dbname)

# Include all modules that define our Flask route-handling functions.
from app.routes import user
from app.routes import admin
from app.routes import editor
from app.routes import traveller
from app.routes import event

# Add a root route
@app.route('/')
def index():
    return redirect(url_for('login'))