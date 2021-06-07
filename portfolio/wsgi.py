import os
import sys
sys.path.append('/home/bitnami/projects/portfolio')
os.environ.setdefault("PYTHON_EGG_CACHE", "/home/bitnami/projects/portfolio/egg_cache")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
