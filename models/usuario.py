from extensions import db
from datetime import datetime


class Usuario(db.Model):
    __tablename__ = "usuarios"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nome = db.Column(
        db.String(100),
        nullable=False
    )

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    senha = db.Column(
        db.String(255),
        nullable=False
    )

    tipo = db.Column(
        db.String(20),
        nullable=False,
        default="usuario"
    )

    data_criacao = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    reclamacoes = db.relationship(
        "Reclamacao",
        back_populates="usuario",
        lazy=True,
        cascade="all, delete-orphan"
    )

    respostas = db.relationship(
        "Resposta",
        back_populates="administrador",
        lazy=True
    )

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "tipo": self.tipo,
            "data_criacao": self.data_criacao.strftime("%d/%m/%Y %H:%M")
        }