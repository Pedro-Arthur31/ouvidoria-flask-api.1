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
    """
    Criar uma nova reclamação
    ---
    tags:
      - Reclamações

    security:
      - Bearer: []

    consumes:
      - application/json

    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - titulo
            - descricao
          properties:
            titulo:
              type: string
              example: Internet indisponível

            descricao:
              type: string
              example: Estou sem internet desde ontem.

    responses:
      201:
        description: Reclamação criada com sucesso

      400:
        description: Dados inválidos

      401:
        description: Usuário não autenticado
    """
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
    """
    Lista reclamações
    ---
    tags:
      - Reclamações

    security:
      - Bearer: []

    responses:
      200:
        description: Lista de reclamações

      401:
        description: Não autenticado
    """
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
    """
    Buscar reclamação pelo ID
    ---
    tags:
      - Reclamações

    security:
      - Bearer: []

    parameters:
      - in: path
        name: id
        type: integer
        required: true
        description: ID da reclamação

    responses:
      200:
        description: Reclamação encontrada

      403:
        description: Acesso negado

      404:
        description: Reclamação não encontrada
    """
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
    """
    Lista as reclamações do usuário logado
    ---
    tags:
      - Reclamações

    security:
      - Bearer: []

    responses:
      200:
        description: Lista das reclamações do usuário
    """
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
    """
Alterar status da reclamação
---
tags:
  - Reclamações

security:
  - Bearer: []

parameters:
  - in: path
    name: id
    type: integer
    required: true

  - in: body
    name: body
    schema:
      type: object
      required:
        - status
      properties:
        status:
          type: string
          example: respondida

responses:
  200:
    description: Status atualizado

  400:
    description: Status inválido

  403:
    description: Apenas administradores
"""
    try:

        dados = request.get_json()

        validar_status(dados["status"])

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
@reclamacao_bp.route("/reclamacoes/<int:id>", methods=["PUT"])
@jwt_required()
def atualizar_reclamacao_route(id):
    """
    Atualiza uma reclamação
    ---
    tags:
      - Reclamações

    security:
      - Bearer: []

    parameters:
      - in: path
        name: id
        type: integer
        required: true

      - in: body
        name: body
        schema:
          type: object
          properties:
            titulo:
              type: string
              example: Internet lenta

            descricao:
              type: string
              example: A velocidade caiu bastante.

    responses:
      200:
        description: Reclamação atualizada

      403:
        description: Sem permissão

      404:
        description: Reclamação não encontrada
    """
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

        if reclamacao.status == "fechada":
            return jsonify({
                "erro": "Reclamação fechada não pode ser alterada."
            }), 403

        dados = request.get_json()

        validar_atualizacao_reclamacao(dados)

        atualizar_reclamacao_service(
            reclamacao,
            dados
        )

        return jsonify({
            "mensagem": "Reclamação atualizada com sucesso."
        }), 200

    except ValueError as erro:

        return jsonify({
            "erro": str(erro)
        }), 400
@reclamacao_bp.route("/reclamacoes/<int:id>", methods=["DELETE"])
@jwt_required()
def excluir_reclamacao_route(id):
    """
    Excluir reclamação
    ---
    tags:
      - Reclamações

    security:
      - Bearer: []

    parameters:
      - in: path
        name: id
        type: integer
        required: true

    responses:
      200:
        description: Reclamação removida

      403:
        description: Sem permissão

      404:
        description: Reclamação não encontrada
    """
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

        excluir_reclamacao_service(
            reclamacao
        )

        return jsonify({
            "mensagem": "Reclamação removida com sucesso."
        }), 200

    except ValueError as erro:

        return jsonify({
            "erro": str(erro)
        }), 404