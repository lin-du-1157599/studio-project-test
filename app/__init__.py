# This script runs automatically when our `app` module is first loaded,
# and handles all the setup for our Flask app.
from flask import Flask, redirect, url_for
import os

app = Flask(__name__)

# Set up database connection.
from app.db.connect import dbuser, dbpass, dbhost, dbname
from app.db.db import init_db
init_db(app, dbuser, dbpass, dbhost, dbname)

# Add multiple template search paths to Jinja2 template loader.
# This allows Flask to locate templates stored in different subdirectories under 'templates'.
app.jinja_loader.searchpath.append(os.path.join(app.root_path, 'templates', 'base'))
app.jinja_loader.searchpath.append(os.path.join(app.root_path, 'templates', 'auth'))
app.jinja_loader.searchpath.append(os.path.join(app.root_path, 'templates', 'home'))
app.jinja_loader.searchpath.append(os.path.join(app.root_path, 'templates', 'user'))
app.jinja_loader.searchpath.append(os.path.join(app.root_path, 'templates', 'event'))

# Set the "secret key" that our app will use to sign session cookies. This can
# be anything.
# 
# Anyone with access to this key can pretend to be signed in as any user. In a
# real-world project, you wouldn't store this key in your source code. To learn
# about how to manage "secrets" like this in production code, check out
# https://blog.gitguardian.com/how-to-handle-secrets-in-python/
#
# For the purpose of your assignments, you DON'T need to use any of those more
# advanced and secure methods: it's fine to store your secret key in your
# source code like we do here.
app.secret_key = 'Example Secret Key (CHANGE THIS TO YOUR OWN SECRET KEY!)'

# Configure upload folder for event images
from app.config import constants
app.config[constants.IMAGE_UPLOAD_FOLDER] = os.path.join(app.root_path, 'static', 'uploads')
os.makedirs(app.config[constants.IMAGE_UPLOAD_FOLDER], exist_ok=True)

# # Set up database connection.
# from app import connect
# from app import db
# db.init_db(app, connect.dbuser, connect.dbpass, connect.dbhost, connect.dbname,
#            connect.dbport)
#
# # Include all modules that define our Flask route-handling functions.
from app.routes import user
from app.routes import admin
from app.routes import editor
from app.routes import traveller
from app.routes import event

# Add a root route
@app.route('/')
def index():
    return redirect(url_for('login'))