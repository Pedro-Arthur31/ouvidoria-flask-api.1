from datetime import datetime
from extensions import db


class Reclamacao(db.Model):
    __tablename__ = 'reclamacoes'

    id = db.Column(db.Integer, primary_key=True)

    titulo = db.Column(db.String(150), nullable=False)

    descricao = db.Column(db.Text, nullable=False)

    status = db.Column(db.String(20), default="aberta")

    data_criacao = db.Column(db.DateTime,default=datetime.utcnow)

    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)

    def __repr__(self):
        return f"Reclamacao {self.titulo}>"