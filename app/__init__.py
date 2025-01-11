from flask import Flask

def create_app():
    app = Flask(__name__)

    # Importa e registra as rotas
    from app.routes.product_routes import product_bp
    
    app.register_blueprint(product_bp)

    return app
