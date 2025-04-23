from flask import Flask

def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    
    # Configuración
    app.config['SECRET_KEY'] = 'tu-clave-secreta'
    
    # Registrar blueprints/rutas
    from .routes import main_bp
    app.register_blueprint(main_bp)
    
    return app