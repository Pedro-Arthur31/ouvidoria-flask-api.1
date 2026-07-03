from datetime import datetime
from extensions import db

class Resposta(db.Model):
    __tablename__ = "resposta"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    mensagem = db.Column(
        db.Text,
        nullable=False
    )

    data_resposta = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    administrador_id = db.Column(
        db.Integer,
        db.ForeignKey("usuarios.id"),
        nullable=False
    )

    reclamacao_id = db.Column(
        db.Integer,
        db.ForeignKey("reclamacoes.id"),
        nullable=False
    )

    administrador = db.relationship(
        "Usuario",
        foreign_keys=[administrador_id]
    )

    reclamacao = db.relationship(
        "Reclamacao",
        backref="respostas"
    )