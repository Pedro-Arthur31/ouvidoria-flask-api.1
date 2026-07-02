from datetime import datetime

from sqlalchemy import true

from extensions import db


class Administrador(db.Model):
    __tablename__ = "administradores"

    id = db.Column(db.Integer, primary_key=True)

    nome = db.Column(db.String(100), nullable=False)

    email = db.Column(db.String(150), unique=True, nullable=False)

    senha = db.Column(db.String(255), nullable=False)

    perfil = db.Column(db.String(20), default="administrador")

    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)

    respostas = db.relationship("Resposta", backref="administrador", lazy=True)

    def __repr__(self):
        return f"<Administrador {self.nome}>"
