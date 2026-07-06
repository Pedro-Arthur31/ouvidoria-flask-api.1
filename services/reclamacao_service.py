from extensions import db
from models.reclamacao import Reclamacao

def criar_reclamacao_service(titulo, descricao, usuario_id):

    reclamacao = Reclamacao(
        titulo=titulo,
        descricao=descricao,
        usuario_id=usuario_id
    )

    db.session.add(reclamacao)
    db.session.commit()

    return reclamacao

def buscar_reclamacao_service(id):

    return Reclamacao.query.get(id)

def atualizar_reclamacao_service(reclamacao,dados):

    reclamacao.titulo = dados.get('titulo', reclamacao.titulo)

    reclamacao.descricao = dados.get("descricao", reclamacao.descricao)

    db.session.commit()

    return reclamacao

def excluir_reclamacao_service(reclamacao):
    db.session.delete(reclamacao)
    db.session.commit()

def listar_reclamacoes_service():

    return Reclamacao.query.all()
def listar_reclamacoes_usuario_service(usuario_id):

    return Reclamacao.query.filter_by(
        usuario_id=usuario_id
    ).all()

def atualizar_status_service(reclamacao, novo_status):
    reclamacao.status = novo_status
    db.session.commit()
    return reclamacao