from flask import Flask
from . import views

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "KEYSMASH FJAFJKLDSKF7JKFDJ 1530"
    app.register_blueprint(views.main_bp)
    return app