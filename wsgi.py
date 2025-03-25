import sys
import os

# Add the application directory to the Python path
path = os.path.dirname(os.path.abspath(__file__))
if path not in sys.path:
    sys.path.insert(0, path)

# Set the working directory
os.chdir(path)

# Print debugging information
print("Python path:", sys.path)
print("Current working directory:", os.getcwd())
print("Files in current directory:", os.listdir())

# Import the Flask application
from app import app as application 