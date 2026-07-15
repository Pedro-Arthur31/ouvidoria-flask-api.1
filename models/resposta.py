from extensions import db
from datetime import datetime


class Resposta(db.Model):
    __tablename__ = "Respostas"

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
        db.ForeignKey("Usuários.id"),
        nullable=False
    )

    reclamacao_id = db.Column(
        db.Integer,
        db.ForeignKey("Reclamações.id"),
        nullable=False
    )

    administrador = db.relationship(
        "Usuário",
        back_populates="Respostas"
    )

    reclamacao = db.relationship(
        "Reclamação",
        back_populates="Respostas"
    )

    def to_dict(self):
        return {
            "Id": self.id,
            "Mensagem": self.mensagem,
            "Administrador_id": self.administrador_id,
            "Reclamação_id": self.reclamacao_id,
            "Data_resposta": self.data_resposta.strftime("%d/%m/%Y %H:%M")
        }