import os
import sys
import logging

# Define settings file
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
#from google.appengine.dist import use_library
#use_library('django', '1.2.1')
from appengine_django import InstallAppengineHelperForDjango
from appengine_django import have_django_zip
from appengine_django import django_zip_path
InstallAppengineHelperForDjango()

# Google App Engine imports.
from google.appengine.ext.webapp import util

# Import the part of Django that we use here.
import django.core.handlers.wsgi

def main():	
  if have_django_zip and django_zip_path not in sys.path:
	sys.path.insert(1, django_zip_path)
	
  # Create a Django application for WSGI.
  application = django.core.handlers.wsgi.WSGIHandler()

  # Run the WSGI CGI handler with that application.
  util.run_wsgi_app(application)

if __name__ == '__main__':
  main()
