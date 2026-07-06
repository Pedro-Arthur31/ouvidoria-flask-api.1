from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required,get_jwt_identity

from extensions import db

from models.reclamacao import Reclamacao
from models.resposta import Resposta

from utils.decorators import admin_required
from utils.status import StatusReclamacao

resposta_bp = Blueprint('resposta', __name__)

@resposta_bp.route("/respostas", methods=["POST"])
@jwt_required()
@admin_required
def criar_resposta_route():
    dados = request.get_json()

    validar_criacao_resposta(dados)

    reclamacao = buscar_reclamacao_service(
        dados["reclamacao_id"]
    ),404

    resposta = criar_resposta(

        mensagem=dados["mensagem"],

        administrador_id=get_jwt_identity(),

        reclamacao=reclamacao
    )

    return jsonify(
        resposta.to_dict()
    ),201

@resposta_bp.route("/reclamacoes/<int:id>/respostas", methods=["GET"])
@jwt_required()
def listar_respostas_route(id):

    respostas = listar_respostas_reclamacao(
        id
    )

    return jsonify([
        r.to_dict()
        for r in respostas
    ]), 200

@resposta_bp.route("/respostas/<int:id>", methods=["GET"])
@jwt_required()
def busca_resposta():
    resposta = busca_resposta

    if not resposta:
        return jsonify({
            "erro": "Resposta não encontrada."
        }), 404
    return jsonify({
        "id": resposta.id,
        "mensagem": resposta.mensagem,
        "administrador_id": resposta.administrador_id,
        "reclamacao_id": resposta.reclamacao_id,
        "data_resposta": resposta.data_resposta
    }), 200
@resposta_bp.route("/respostas/<int:id>", methods=["PUT"])
@jwt_required()
@admin_required
def atualizar_resposta(id):

    resposta = buscar_resposta(id)

    if not resposta:
        return jsonify({
            "erro": "Resposta não encontrada."
        }), 404

    validar_atualizacao_resposta(dados)

    atualizar_resposta(
        resposta,
        dados
    )
    return jsonify({
        "mensagem": "Resposta atualizada."
    }), 200
@resposta_bp.route("/respostas/<int:id>", methods=["DELETE"])
@jwt_required()
@admin_required
def deletar_resposta(id):
    resposta = buscar_resposta(id)
    if not resposta:
        return jsonify({
            "erro": "Resposta não encontrada."
        }), 404

    excluir_resposta(
        resposta
    )
    return jsonify({
        "mensagem": "Resposta deletada com sucesso."
    }), 200