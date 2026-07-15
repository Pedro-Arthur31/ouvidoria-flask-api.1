from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from utils.decorators import admin_required
from utils.security import is_admin

from services.usuario_service import (
    criar_usuario,
    listar_usuarios,
    buscar_usuario,
    atualizar_usuario,
    excluir_usuario
)

from validators.usuario_validator import (
    validar_criacao_usuario,
    validar_atualizacao_usuario
)

usuario_bp = Blueprint(
    "Usuário",
    __name__
)



@usuario_bp.route("/usuários", methods=["POST"])
def criar_usuario_route():
    """
    Cadastrar novo usuário
    ---
    tags:
      - Usuários

    consumes:
      - application/json

    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - nome
            - email
            - senha
          properties:
            nome:
              type: string
              example: Pedro Arthur

            email:
              type: string
              example: pedro@email.com

            senha:
              type: string
              example: "123456"

    responses:
      201:
        description: Usuário criado com sucesso.

      400:
        description: Dados inválidos.
    """
    try:

        dados = request.get_json()

        validar_criacao_usuario(dados)

        usuario = criar_usuario(
            nome=dados["nome"],
            email=dados["email"],
            senha=dados["senha"]
        )

        return jsonify(
            usuario.to_dict()
        ), 201

    except ValueError as erro:

        return jsonify({
            "Erro": str(erro)
        }), 400



@usuario_bp.route("/usuários", methods=["GET"])
@jwt_required()
@admin_required
def listar_usuarios_route():
    """
    Lista todos os usuários
    ---
    tags:
      - Usuários

    security:
      - Bearer: []

    responses:
      200:
        description: Lista de usuários

      403:
        description: Apenas administradores
    """
    usuarios = listar_usuarios()

    return jsonify([
        usuario.to_dict()
        for usuario in usuarios
    ]), 200



@usuario_bp.route("/usuários/<int:id>", methods=["GET"])
@jwt_required()
def buscar_usuario_route(id):
    """
    Busca um usuário pelo ID
    ---
    tags:
      - Usuários

    security:
      - Bearer: []

    parameters:
      - in: path
        name: id
        type: integer
        required: true

    responses:
      200:
        description: Usuário encontrado.

      404:
        description: Usuário não encontrado.
    """
    usuario_logado = get_jwt_identity()

    if str(usuario_logado) != str(id) and not is_admin():
        return jsonify({
            "Erro": "Acesso negado."
        }), 403

    usuario = buscar_usuario(id)

    if not usuario:
        return jsonify({
            "Erro": "Usuário não encontrado."
        }), 404

    return jsonify(
        usuario.to_dict()
    ), 200



@usuario_bp.route("/usuários/<int:id>", methods=["PUT"])
@jwt_required()
def atualizar_usuario_route(id):
    """
    Atualiza um usuário
    ---
    tags:
      - Usuários

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
            nome:
              type: string

            email:
              type: string

            senha:
              type: string

    responses:
      200:
        description: Usuário atualizado.
    """
    usuario = buscar_usuario(id)

    if not usuario:
        return jsonify({
            "Erro": "Usuário não encontrado."
        }), 404

    usuario_logado = get_jwt_identity()

    if str(usuario_logado) != str(id) and not is_admin():
        return jsonify({
            "Erro": "Acesso negado."
        }), 403

    dados = request.get_json()

    validar_atualizacao_usuario(dados)

    atualizar_usuario(
        usuario,
        dados
    )

    return jsonify({
        "Mensagem": "Usuário atualizado com sucesso."
    }), 200



@usuario_bp.route("/usuários/<int:id>", methods=["DELETE"])
@jwt_required()
def excluir_usuario_route(id):
    """
    Remove um usuário
    ---
    tags:
      - Usuários

    security:
      - Bearer: []

    parameters:
      - in: path
        name: id
        type: integer
        required: true

    responses:
      200:
        description: Usuário removido.

      404:
        description: Usuário não encontrado.
    """
    usuario = buscar_usuario(id)

    if not usuario:
        return jsonify({
            "Erro": "Usuário não encontrado."
        }), 404

    usuario_logado = get_jwt_identity()

    if str(usuario_logado) != str(id) and not is_admin():
        return jsonify({
            "Erro": "Acesso negado."
        }), 403

    excluir_usuario(usuario)

    return jsonify({
        "Mensagem": "Usuário removido com sucesso."
    }), 200



@usuario_bp.route("/me", methods=["GET"])
@jwt_required()
def meu_perfil_route():
    """
    Perfil do usuário autenticado.
    ---
    tags:
      - Usuários

    security:
      - Bearer: []

    responses:
      200:
        description: Perfil do usuário.
    """
    usuario_id = get_jwt_identity()

    usuario = buscar_usuario(usuario_id)

    if not usuario:
        return jsonify({
            "Erro": "Usuário não encontrado."
        }), 404

    return jsonify(
        usuario.to_dict()
    ), 200



@usuario_bp.route("/admin", methods=["GET"])
@jwt_required()
@admin_required
def painel_admin_route():
    """
    Painel administrativo
    ---
    tags:
      - Administração

    security:
      - Bearer: []

    responses:
      200:
        description: Acesso permitido.

      403:
        description: Apenas administradores.
    """
    usuario_id = get_jwt_identity()

    usuario = buscar_usuario(usuario_id)

    if not usuario:
        return jsonify({
            "Erro": "Usuário não encontrado."
        }), 404

    return jsonify({
        "Mensagem": f"Bem-vindo ao painel administrativo, {usuario.nome}!",
        "Usuário": usuario.to_dict()
    }), 200