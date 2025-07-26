import subprocess
import sys

if __name__ == '__main__':
    print('🚀 Starting Rio + Django Task Manager in development mode...')
    print('📱 Rio UI: http://localhost:8080')
    print('🔧 Django Admin: http://localhost:8080/admin')
    print('🔌 API Endpoints: http://localhost:8080/api')
    print('🔄 Auto-reload enabled')

    try:
        subprocess.run(
            [
                sys.executable,
                '-m',
                'uvicorn',
                'main:app',
                '--host',
                '0.0.0.0',
                '--port',
                '8080',
                '--reload',
            ]
        )
    except KeyboardInterrupt:
        print('\n👋 Server stopped')
