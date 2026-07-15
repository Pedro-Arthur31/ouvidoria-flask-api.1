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
    "Resposta",
    __name__
)

@resposta_bp.route("/respostas", methods=["POST"])
@jwt_required()
@admin_required
def criar_resposta_route():
    """
    Criar uma resposta para uma reclamação
    ---
    tags:
      - Respostas

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
            - reclamacao_id
            - mensagem
          properties:
            reclamacao_id:
              type: integer
              example: 1

            mensagem:
              type: string
              example: Sua solicitação foi encaminhada ao setor responsável.

    responses:
      201:
        description: Resposta criada com sucesso.

      400:
        description: Dados inválidos.

      403:
        description: Apenas administradores.

      404:
        description: Reclamação não encontrada.
    """
    try:

        dados = request.get_json()

        validar_criacao_resposta(dados)

        reclamacao = buscar_reclamacao_service(
            dados["Reclamação_id"]
        )

        resposta = criar_resposta(
            mensagem=dados["Mensagem"],
            administrador_id=get_jwt_identity(),
            reclamacao=reclamacao
        )

        return jsonify(
            resposta.to_dict()
        ), 201

    except ValueError as erro:

        return jsonify({
            "Erro": str(erro)
        }), 400
@resposta_bp.route("/reclamações/<int:id>/respostas", methods=["GET"])
@jwt_required()
def listar_respostas_route(id):
    """
    Lista todas as respostas de uma reclamação
    ---
    tags:
      - Respostas

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
        description: Lista de respostas.

      404:
        description: Reclamação não encontrada.
    """
    try:

        respostas = listar_respostas_reclamacao(id)

        return jsonify([
            resposta.to_dict()
            for resposta in respostas
        ]), 200

    except Exception as erro:

        return jsonify({
            "Erro": str(erro)
        }), 500
@resposta_bp.route("/respostas/<int:id>", methods=["GET"])
@jwt_required()
def buscar_resposta_route(id):
    """
    Buscar resposta pelo ID
    ---
    tags:
      - Respostas

    security:
      - Bearer: []

    parameters:
      - in: path
        name: id
        type: integer
        required: true

    responses:
      200:
        description: Resposta encontrada.

      404:
        description: Resposta não encontrada.
    """
    try:

        resposta = buscar_resposta(id)

        return jsonify(
            resposta.to_dict()
        ), 200

    except ValueError as erro:

        return jsonify({
            "Erro": str(erro)
        }), 404
@resposta_bp.route("/respostas/<int:id>", methods=["PUT"])
@jwt_required()
@admin_required
def atualizar_resposta_route(id):
    """
    Atualizar resposta
    ---
    tags:
      - Respostas

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
            mensagem:
              type: string
              example: A solicitação já foi resolvida.

    responses:
      200:
        description: Resposta atualizada.

      403:
        description: Apenas administradores.

      404:
        description: Resposta não encontrada.
    """
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
            "Erro": str(erro)
        }), 400
@resposta_bp.route("/respostas/<int:id>", methods=["DELETE"])
@jwt_required()
@admin_required
def deletar_resposta_route(id):
    """
    Excluir resposta
    ---
    tags:
      - Respostas

    security:
      - Bearer: []

    parameters:
      - in: path
        name: id
        type: integer
        required: true

    responses:
      200:
        description: Resposta removida.

      403:
        description: Apenas administradores.

      404:
        description: Resposta não encontrada.
    """
    try:

        resposta = buscar_resposta(id)

        excluir_resposta(resposta)

        return jsonify({
            "Mensagem": "Resposta removida com sucesso."
        }), 200

    except ValueError as erro:

        return jsonify({
            "Erro": str(erro)
        }), 404