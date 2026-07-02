from datetime import datetime
from extensions import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)

    nome = db.Column (db.String(100),nullable=False)

    email = db.Column (db.String(150),unique=True,nullable=False)

    senha = db.Column (db.String(255),nullable=False)

    perfil = db.Column (db.String(20),default="usuario")

    data_criacao = db.Column (db.DateTime,default=datetime.utcnow)

    def __repr__(self):
        return f'<Usuario {self.nome}>'

    reclamacoes = db.relationship(
        "Reclamacao",
        backref="usuario",
        lazy=True
    )