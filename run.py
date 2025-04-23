from werkzeug.middleware.dispatcher import DispatcherMiddleware
from backend.app import create_app as create_backend_app
from frontend.app import create_app as create_frontend_app
from werkzeug.serving import run_simple

# Crear las aplicaciones
backend_app = create_backend_app()  # De backend
frontend_app = create_frontend_app()  # De frontend


# Verificar que las aplicaciones están bien configuradas
assert backend_app is not None, "Backend app no se creó correctamente."
assert frontend_app is not None, "Frontend app no se creó correctamente."

# Configurar DispatcherMiddleware
app = DispatcherMiddleware(frontend_app, {
    '/api': backend_app
})
application = app


if __name__ == "__main__":
    run_simple('localhost', 5000, application, use_reloader=True)
#Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process