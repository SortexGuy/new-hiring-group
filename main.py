import os
import django
from importlib.util import find_spec
from django.core.management import execute_from_command_line
from django.core.wsgi import get_wsgi_application
import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.wsgi import WSGIMiddleware

# Import Rio app after Django setup
from app import app as rio_app

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')
django.setup()


def run_django_migrations():
    """Run Django migrations on startup"""
    try:
        execute_from_command_line(['manage.py', 'migrate'])
    except:
        print('Note: Migrations will be run when you create manage.py')


def create_fastapi_app():
    """Create FastAPI app that integrates Django and Rio"""
    # Run migrations
    run_django_migrations()

    # Create FastAPI app
    fastapi_app = FastAPI(title='Rio + Django Task Manager')

    # Mount Django WSGI app for API endpoints
    django_app = get_wsgi_application()
    fastapi_app.mount('/dj', WSGIMiddleware(django_app))
    fastapi_app.mount(
        '/static',
        StaticFiles(
            directory=os.path.normpath(
                os.path.join(
                    find_spec('django.contrib.admin').origin, '..', 'static'
                )
            ),
            follow_symlink=True,
        ),
        name='static',
    )

    # Convert Rio app to FastAPI and mount it
    rio_fastapi = rio_app.as_fastapi()
    fastapi_app.mount('/', rio_fastapi)

    return fastapi_app


# Create the app instance at module level for uvicorn
app = create_fastapi_app()

if __name__ == '__main__':
    print('🚀 Starting Rio + Django Task Manager...')
    print('📱 Rio UI: http://localhost:8080')
    print('🔧 Django Admin: http://localhost:8080/admin')
    print('🔌 API Endpoints: http://localhost:8080/api')
    print('\n💡 For development with auto-reload, run:')
    print('   uvicorn main:app --host 127.0.0.1 --port 8080 --reload')

    # Run with Uvicorn (without reload to avoid the error)
    uvicorn.run(app, host='127.0.0.1', port=8080, reload=False)
