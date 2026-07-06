from flask import Flask
from extensions import db
from routes.usuario_routes import usuario_bp
from flask_jwt_extended import JWTManager
from routes.auth_routes import auth_bp
from datetime import timedelta
from routes.reclamacao_routes import reclamacao_bp
from routes.resposta_routes import resposta_bp

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mysql+pymysql://root:root@localhost/ouvidoria_db"
)
app.register_blueprint(usuario_bp)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


app.config["JWT_SECRET_KEY"] = "minha_chave_de_api_julia"
db.init_app(app)
jwt = JWTManager(app)

app.register_blueprint(auth_bp)

app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)

app.register_blueprint(reclamacao_bp)

app.register_blueprint(resposta_bp)

with app.app_context():
    db.create_all()
    print("Tabelas criadas!")

@app.route("/")
def home():
    return {"mensagem": "API da Ouvidoria funcionando"}

if __name__ == "__main__":
    app.run(debug=True)