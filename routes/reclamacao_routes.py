from flask import Blueprint, request, jsonify

from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)

from utils.decorators import admin_required
from utils.security import is_admin

from services.reclamacao_service import (
    criar_reclamacao_service,
    listar_reclamacoes_service,
    listar_reclamacoes_usuario_service,
    buscar_reclamacao_service,
    atualizar_reclamacao_service,
    atualizar_status_service,
    excluir_reclamacao_service
)

from validators.reclamacao_validator import (
    validar_criacao_reclamacao,
    validar_atualizacao_reclamacao,
    validar_status
)

reclamacao_bp = Blueprint(
    "reclamacao",
    __name__
)
@reclamacao_bp.route("/reclamacoes", methods=["POST"])
@jwt_required()
def criar_reclamacao_route():

    try:

        dados = request.get_json()

        validar_criacao_reclamacao(dados)

        usuario_id = get_jwt_identity()

        reclamacao = criar_reclamacao_service(
            titulo=dados["titulo"],
            descricao=dados["descricao"],
            usuario_id=usuario_id
        )

        return jsonify(
            reclamacao.to_dict()
        ), 201

    except ValueError as erro:

        return jsonify({
            "erro": str(erro)
        }), 400

@reclamacao_bp.route("/reclamacoes", methods=["GET"])
@jwt_required()
def listar_reclamacoes_route():

    try:

        usuario_id = get_jwt_identity()

        if is_admin():

            reclamacoes = listar_reclamacoes_service()

        else:

            reclamacoes = listar_reclamacoes_usuario_service(
                usuario_id
            )

        return jsonify([
            reclamacao.to_dict()
            for reclamacao in reclamacoes
        ]), 200

    except Exception as erro:

        return jsonify({
            "erro": str(erro)
        }), 500
@reclamacao_bp.route("/reclamacoes/<int:id>", methods=["GET"])
@jwt_required()
def buscar_reclamacao_route(id):

    try:

        reclamacao = buscar_reclamacao_service(id)

        usuario_id = get_jwt_identity()

        if (
            str(reclamacao.usuario_id) != str(usuario_id)
            and not is_admin()
        ):
            return jsonify({
                "erro": "Acesso negado."
            }), 403

        return jsonify(
            reclamacao.to_dict()
        ), 200

    except ValueError as erro:

        return jsonify({
            "erro": str(erro)
        }), 404
@reclamacao_bp.route("/minhas-reclamacoes", methods=["GET"])
@jwt_required()
def minhas_reclamacoes_route():

    try:

        usuario_id = get_jwt_identity()

        reclamacoes = listar_reclamacoes_usuario_service(
            usuario_id
        )

        return jsonify([
            reclamacao.to_dict()
            for reclamacao in reclamacoes
        ]), 200

    except Exception as erro:

        return jsonify({
            "erro": str(erro)
        }), 500
@reclamacao_bp.route("/reclamacoes/<int:id>/status", methods=["PATCH"])
@jwt_required()
@admin_required
def alterar_status_route(id):

    try:

        dados = request.get_json()

        validar_status(dados)

        reclamacao = buscar_reclamacao_service(id)

        atualizar_status_service(
            reclamacao,
            dados["status"]
        )

        return jsonify({
            "mensagem": "Status atualizado com sucesso.",
            "status": reclamacao.status
        }), 200

    except ValueError as erro:

        return jsonify({
            "erro": str(erro)
        }), 400