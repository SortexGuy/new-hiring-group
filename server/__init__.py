import os
from importlib.util import find_spec

from .wsgi import application
from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi.staticfiles import StaticFiles
from ..app import app as rioApp

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myapp.settings')
os.environ.setdefault('DJANGO_CONFIGURATIN', 'Localdev')

app = rioApp.as_fastapi()
app.mount('/admin', WSGIMiddleware(application))
app.mount(
    '/static',
    StaticFiles(
        directory=os.path.normpath(
            os.path.join(
                find_spec('django.contrib.admin').origin, '..', 'static'
            )
        )
    ),
    name='static',
)
