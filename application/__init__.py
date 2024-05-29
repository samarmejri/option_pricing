from flask import Flask

def create_app():
    app = Flask(__name__)

    from application.routes.option_routes import option_routes
    app.register_blueprint(option_routes)

    return app
