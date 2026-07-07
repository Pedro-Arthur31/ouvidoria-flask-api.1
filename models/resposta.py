from extensions import db
from datetime import datetime


class Resposta(db.Model):
    __tablename__ = "respostas"

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
        default=datetime.utcnow,
        nullable=False
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
        back_populates="respostas"
    )

    reclamacao = db.relationship(
        "Reclamacao",
        back_populates="respostas"
    )

    def to_dict(self):
        return {
            "id": self.id,
            "mensagem": self.mensagem,
            "administrador_id": self.administrador_id,
            "reclamacao_id": self.reclamacao_id,
            "data_resposta": self.data_resposta.strftime("%d/%m/%Y %H:%M")
        }