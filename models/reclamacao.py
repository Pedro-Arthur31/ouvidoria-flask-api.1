from extensions import db
from datetime import datetime


class Reclamacao(db.Model):
    __tablename__ = "reclamacoes"

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
        default="aberta"
    )

    data_criacao = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    usuario_id = db.Column(
        db.Integer,
        db.ForeignKey("usuarios.id"),
        nullable=False
    )

    usuario = db.relationship(
        "Usuario",
        back_populates="reclamacoes"
    )

    respostas = db.relationship(
        "Resposta",
        back_populates="reclamacao",
        lazy=True,
        cascade="all, delete-orphan"
    )

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "status": self.status,
            "usuario_id": self.usuario_id,
            "data_criacao": self.data_criacao.strftime("%d/%m/%Y %H:%M")
        }