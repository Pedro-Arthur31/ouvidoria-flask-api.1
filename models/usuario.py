from datetime import datetime
from extensions import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)

    nome = db.Column (db.String(100),nullable=False)

    email = db.Column (db.String(150),unique=True,nullable=False)

    senha = db.Column (db.String(255),nullable=False)

    tipo = db.Column (db.String(20),default="usuario")

    data_criacao = db.Column (db.DateTime,default=datetime.utcnow,nullable=False)

    def __repr__(self):
        return f'<Usuario {self.nome}>'

    reclamacoes = db.relationship(
        "Reclamacao",
        back_populates="usuario",
        cascade="all, delete-orphan",
    )
    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "tipo": self.tipo,
            "data_criacao": self.data_criacao.isoformat()
        }