from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from extensions import db
from models.reclamacao import Reclamacao

reclamacao_bp = Blueprint(
    "reclamacao",
    __name__,
)

@reclamacao_bp.route(
    "/reclamacoes",
    methods=["POST"]
)

@jwt_required()
def criar_reclamacao():
    dados = request.get_json()

    usuario_id = get_jwt_identity()

    nova_reclamacao = Reclamacao(
        titulo=dados["titulo"],
        descricao=dados["descricao"],
        usuario_id=usuario_id
    )

    db.session.add(
        nova_reclamacao
    )

    db.session.commit()

    return jsonify({
        "Parabens": "Reclamação criada com sucesso"
    }), 201

@reclamacao_bp.route("/reclamacoes", methods=["GET"])

@jwt_required()
def listar_reclamacao():

    reclamacoes = Reclamacao.query.all()

    lista = []

    for reclamacao in reclamacoes:
        lista.append({
            "id": reclamacao.id,
            "titulo": reclamacao.titulo,
            "descricao": reclamacao.descricao,
            "status": reclamacao.status,
            "usuario_id": reclamacao.usuario_id
        })

        return jsonify(lista), 200

@reclamacao_bp.route("/minhas-reclamacoes", methods=["GET"])
@jwt_required()
def minha_reclamacoes():

    usuario_id = get_jwt_identity()

    reclamacoes = Reclamacao.query.filter_by(usuario_id=usuario_id).all()

    lista = []

    for reclamacao in reclamacoes:
        lista.append({
            "id": reclamacao.id,
            "titulo": reclamacao.titulo,
            "status": reclamacao.status,
        })

        return jsonify(lista), 200