from datetime import timedelta

from flask import Flask
from flask_jwt_extended import JWTManager
from sqlalchemy import text
from extensions import db
from config import Config

from routes.auth_routes import auth_bp
from routes.usuario_routes import usuario_bp
from routes.reclamacao_routes import reclamacao_bp
from routes.resposta_routes import resposta_bp

from flasgger import Swagger

app = Flask(__name__)
app.config["SWAGGER"] = {
    "title": "API Ouvidoria",
    "uiversion": 3
}

app.config.from_object(Config)


db.init_app(app)

jwt = JWTManager(app)
template = {
    "swagger": "2.0",
    "info": {
        "title": "API Ouvidoria",
        "description": "API REST desenvolvida com Flask, JWT e MySQL.",
        "version": "1.0.0"
    },
    "securityDefinitions": {
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": "Digite: Bearer <seu_token>"
        }
    }
}

swagger = Swagger(app, template=template)


app.register_blueprint(auth_bp)
app.register_blueprint(usuario_bp)
app.register_blueprint(reclamacao_bp)
app.register_blueprint(resposta_bp)



with app.app_context():
    db.create_all()
    print("Tabelas criadas com sucesso!")



@app.route("/")
def home():
    return {
        "Mensagem": "API da Ouvidoria funcionando.",
        "Versao": "1.0.0",
        "Status": "online"
    }

