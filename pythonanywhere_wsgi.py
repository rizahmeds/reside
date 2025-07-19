import os
import sys

# Add the project path to the system path
path = '/home/your-username/reside'  # Use your PythonAnywhere username
if path not in sys.path:
    sys.path.insert(0, path)

# Add the src directory to the system path
src_path = '/home/your-username/reside/src'
if src_path not in sys.path:
    sys.path.insert(0, src_path)

# Set the settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'reside.settings'

# Import the Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
