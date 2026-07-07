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
    "usuario",
    __name__
)



@usuario_bp.route("/usuarios", methods=["POST"])
def criar_usuario_route():

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
            "erro": str(erro)
        }), 400



@usuario_bp.route("/usuarios", methods=["GET"])
@jwt_required()
@admin_required
def listar_usuarios_route():

    usuarios = listar_usuarios()

    return jsonify([
        usuario.to_dict()
        for usuario in usuarios
    ]), 200



@usuario_bp.route("/usuarios/<int:id>", methods=["GET"])
@jwt_required()
def buscar_usuario_route(id):

    usuario_logado = get_jwt_identity()

    if str(usuario_logado) != str(id) and not is_admin():
        return jsonify({
            "erro": "Acesso negado."
        }), 403

    usuario = buscar_usuario(id)

    if not usuario:
        return jsonify({
            "erro": "Usuário não encontrado."
        }), 404

    return jsonify(
        usuario.to_dict()
    ), 200



@usuario_bp.route("/usuarios/<int:id>", methods=["PUT"])
@jwt_required()
def atualizar_usuario_route(id):

    usuario = buscar_usuario(id)

    if not usuario:
        return jsonify({
            "erro": "Usuário não encontrado."
        }), 404

    usuario_logado = get_jwt_identity()

    if str(usuario_logado) != str(id) and not is_admin():
        return jsonify({
            "erro": "Acesso negado."
        }), 403

    dados = request.get_json()

    validar_atualizacao_usuario(dados)

    atualizar_usuario(
        usuario,
        dados
    )

    return jsonify({
        "mensagem": "Usuário atualizado com sucesso."
    }), 200



@usuario_bp.route("/usuarios/<int:id>", methods=["DELETE"])
@jwt_required()
def excluir_usuario_route(id):

    usuario = buscar_usuario(id)

    if not usuario:
        return jsonify({
            "erro": "Usuário não encontrado."
        }), 404

    usuario_logado = get_jwt_identity()

    if str(usuario_logado) != str(id) and not is_admin():
        return jsonify({
            "erro": "Acesso negado."
        }), 403

    excluir_usuario(usuario)

    return jsonify({
        "mensagem": "Usuário removido com sucesso."
    }), 200



@usuario_bp.route("/me", methods=["GET"])
@jwt_required()
def meu_perfil_route():

    usuario_id = get_jwt_identity()

    usuario = buscar_usuario(usuario_id)

    if not usuario:
        return jsonify({
            "erro": "Usuário não encontrado."
        }), 404

    return jsonify(
        usuario.to_dict()
    ), 200



@usuario_bp.route("/admin", methods=["GET"])
@jwt_required()
@admin_required
def painel_admin_route():

    usuario_id = get_jwt_identity()

    usuario = buscar_usuario(usuario_id)

    if not usuario:
        return jsonify({
            "erro": "Usuário não encontrado."
        }), 404

    return jsonify({
        "mensagem": f"Bem-vindo ao painel administrativo, {usuario.nome}!",
        "usuario": usuario.to_dict()
    }), 200