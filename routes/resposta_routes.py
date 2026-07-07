from flask import Blueprint, request, jsonify

from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)

from utils.decorators import admin_required

from services.resposta_service import (
    criar_resposta,
    listar_respostas_reclamacao,
    buscar_resposta,
    atualizar_resposta,
    excluir_resposta
)

from services.reclamacao_service import (
    buscar_reclamacao_service
)

from validators.resposta_validator import (
    validar_criacao_resposta,
    validar_atualizacao_resposta
)

resposta_bp = Blueprint(
    "resposta",
    __name__
)

@resposta_bp.route("/respostas", methods=["POST"])
@jwt_required()
@admin_required
def criar_resposta_route():

    try:

        dados = request.get_json()

        validar_criacao_resposta(dados)

        reclamacao = buscar_reclamacao_service(
            dados["reclamacao_id"]
        )

        resposta = criar_resposta(
            mensagem=dados["mensagem"],
            administrador_id=get_jwt_identity(),
            reclamacao=reclamacao
        )

        return jsonify(
            resposta.to_dict()
        ), 201

    except ValueError as erro:

        return jsonify({
            "erro": str(erro)
        }), 400
@resposta_bp.route("/reclamacoes/<int:id>/respostas", methods=["GET"])
@jwt_required()
def listar_respostas_route(id):

    try:

        respostas = listar_respostas_reclamacao(id)

        return jsonify([
            resposta.to_dict()
            for resposta in respostas
        ]), 200

    except Exception as erro:

        return jsonify({
            "erro": str(erro)
        }), 500
@resposta_bp.route("/respostas/<int:id>", methods=["GET"])
@jwt_required()
def buscar_resposta_route(id):

    try:

        resposta = buscar_resposta(id)

        return jsonify(
            resposta.to_dict()
        ), 200

    except ValueError as erro:

        return jsonify({
            "erro": str(erro)
        }), 404
@resposta_bp.route("/respostas/<int:id>", methods=["PUT"])
@jwt_required()
@admin_required
def atualizar_resposta_route(id):

    try:

        resposta = buscar_resposta(id)

        dados = request.get_json()

        validar_atualizacao_resposta(dados)

        resposta = atualizar_resposta(
            resposta,
            dados
        )

        return jsonify(
            resposta.to_dict()
        ), 200

    except ValueError as erro:

        return jsonify({
            "erro": str(erro)
        }), 400
@resposta_bp.route("/respostas/<int:id>", methods=["DELETE"])
@jwt_required()
@admin_required
def deletar_resposta_route(id):

    try:

        resposta = buscar_resposta(id)

        excluir_resposta(resposta)

        return jsonify({
            "mensagem": "Resposta removida com sucesso."
        }), 200

    except ValueError as erro:

        return jsonify({
            "erro": str(erro)
        }), 404