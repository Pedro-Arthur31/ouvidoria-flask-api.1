from extensions import db
from datetime import datetime


class Reclamacao(db.Model):
    __tablename__ = "Reclamações"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    titulo = db.Column(
        db.String(150),
        nullable=False
    )

    descricao = db.Column(
        db.Text,
        nullable=False
    )

    status = db.Column(
        db.String(30),
        nullable=False,
        default="Aberta"
    )

    data_criacao = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    usuario_id = db.Column(
        db.Integer,
        db.ForeignKey("Usuários.id"),
        nullable=False
    )

    usuario = db.relationship(
        "Usuário",
        back_populates="Reclamações"
    )

    respostas = db.relationship(
        "Resposta",
        back_populates="Reclamação",
        lazy=True,
        cascade="all, delete-orphan"
    )

    def to_dict(self):
        return {
            "Id": self.id,
            "Título": self.titulo,
            "Descricão": self.descricao,
            "Status": self.status,
            "Usuário_id": self.usuario_id,
            "Data_criacão": self.data_criacao.strftime("%d/%m/%Y %H:%M")
        }