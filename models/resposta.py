from datetime import datetime
from extensions import db

class Resposta(db.Model):
    __tablename__ = "resposta"

    id = db.Column(db.Integer, primary_key=True)

    mensagem = db.Column(db.Text, nullable=False)

    data_resposta = db.Column(db.DateTime, default=datetime.utcnow)

    administrador_id = db.Column(db.Integer, db.ForeignKey('administradores.id'), nullable=False)


    reclamacao_id = db.Column(db.Integer, db.ForeignKey('reclamacoes.id'), nullable=False)

    def __repr__(self):
        return f"<Resposta {self.id}>"