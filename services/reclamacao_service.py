from extensions import db

from models.reclamacao import Reclamacao


def criar_reclamacao_service(
        titulo,
        descricao,
        usuario_id
):

    reclamacao = Reclamacao(
        titulo=titulo,
        descricao=descricao,
        usuario_id=usuario_id
    )

    db.session.add(reclamacao)

    db.session.commit()

    return reclamacao


def listar_reclamacoes_service():

    return Reclamacao.query.all()


def listar_reclamacoes_usuario_service(usuario_id):

    return Reclamacao.query.filter_by(
        usuario_id=usuario_id
    ).all()


def buscar_reclamacao_service(id):

    reclamacao = Reclamacao.query.get(id)

    if not reclamacao:
        raise ValueError("Reclamação não encontrada.")

    return reclamacao


def atualizar_reclamacao_service(
        reclamacao,
        dados
):

    if "Título" in dados:
        reclamacao.titulo = dados["Título"]

    if "Descrição" in dados:
        reclamacao.descricao = dados["Descrição"]

    db.session.commit()

    return reclamacao


def atualizar_status_service(
        reclamacao,
        novo_status
):

    reclamacao.status = novo_status

    db.session.commit()

    return reclamacao


def excluir_reclamacao_service(reclamacao):

    db.session.delete(reclamacao)

    db.session.commit()