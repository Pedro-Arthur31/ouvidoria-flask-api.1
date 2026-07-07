from extensions import db

from models.resposta import Resposta

from utils.status import StatusReclamacao


def criar_resposta(
        mensagem,
        administrador_id,
        reclamacao
):

    resposta = Resposta(
        mensagem=mensagem,
        administrador_id=administrador_id,
        reclamacao_id=reclamacao.id
    )

    reclamacao.status = StatusReclamacao.RESPONDIDA.value

    db.session.add(resposta)

    db.session.commit()

    return resposta


def listar_respostas_reclamacao(id):

    return Resposta.query.filter_by(
        reclamacao_id=id
    ).all()


def buscar_resposta(id):

    resposta = Resposta.query.get(id)

    if not resposta:
        raise ValueError("Resposta não encontrada.")

    return resposta


def atualizar_resposta(
        resposta,
        dados
):

    if "mensagem" in dados:
        resposta.mensagem = dados["mensagem"]

    db.session.commit()

    return resposta


def excluir_resposta(resposta):

    db.session.delete(resposta)

    db.session.commit()