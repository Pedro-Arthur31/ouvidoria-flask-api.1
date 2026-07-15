from extensions import db
from datetime import datetime


class Usuario(db.Model):
    __tablename__ = "Usuários"

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
        default="Usuário"
    )

    data_criacao = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    reclamacoes = db.relationship(
        "Reclamação",
        back_populates="Usuário",
        lazy=True,
        cascade="all, delete-orphan"
    )

    respostas = db.relationship(
        "Resposta",
        back_populates="Administrador",
        lazy=True
    )

    def to_dict(self):
        return {
            "Id": self.id,
            "Nome": self.nome,
            "Email": self.email,
            "Tipo": self.tipo,
            "Data_criação": self.data_criacao.strftime("%d/%m/%Y %H:%M")
        }