from datetime import timedelta

from flask import Flask
from flask_jwt_extended import JWTManager

from extensions import db
from config import Config

from routes.auth_routes import auth_bp
from routes.usuario_routes import usuario_bp
from routes.reclamacao_routes import reclamacao_bp
from routes.resposta_routes import resposta_bp


app = Flask(__name__)


app.config.from_object(Config)


db.init_app(app)

jwt = JWTManager(app)



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
        "mensagem": "API da Ouvidoria funcionando.",
        "versao": "1.0.0",
        "status": "online"
    }


if __name__ == "__main__":
    app.run(debug=True)