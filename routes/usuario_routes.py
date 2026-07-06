from flask import Blueprint, request, jsonify

from werkzeug.security import generate_password_hash
from flask_jwt_extended import jwt_required, get_jwt_identity

from utils.decorators import admin_required


from services.usuario_service import *


usuario_bp = Blueprint("usuario", __name__)

@usuario_bp.route("/usuarios", methods=["POST"])
def criar_usuario_route():
    try:

        validar_criacao_usuario(dados)

        usuario = criar_usuario(
            nome,
            email,
            senha
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
def buscar_usuario_routes(id):

    try:
        usuario_logado = get_jwt_identity()

        if str(usuario_logado) != str(id) and not is_admin():
            return jsonify({
                "erro": "Acesso negado."
            }), 403

        usuario = buscar_usuario(id)

        if not usuario:
            return jsonify({
                "erro": "Usuário não encontrado"
            }), 404
        return jsonify(usuario.to_dict()),200

    except Exception as erro:
        return jsonify({
            "erro": str(erro)
        }),500
@usuario_bp.route("/usuarios/<int:id>", methods=["PUT"])
@jwt_required()
def atualizar_usuario_routes(id):
    try:
        usuario = Usuario.query.get(id)
        usuario_logado = get_jwt_identity()

        if (
                str(usuario_logado) != str(id)
                and not is_admin()
        ):
            return jsonify({
                "erro": "Acesso negado."
            }), 403

        if not usuario:
            return jsonify({
                "erro": "Usuário não encontrado"
            }), 404

        dados = request.get_json()

        atualizar_usuario(
            usuario,
            dados
        )

        return jsonify({
            "mensagem": "Usuário atualizado com sucesso."
        }), 200

    except Exception as erro:
        return jsonify({
            "erro": str(erro)
        }), 500
@usuario_bp.route("/usuarios/<int:id>", methods=["DELETE"])
@jwt_required()
def deletar_usuario_routes(id):
    try:
        usuario = Usuario.query.get(id)
        usuario_logado = get_jwt_identity()

        if (
                str(usuario_logado) != str(id)
                and not is_admin()
        ):
            return jsonify({
                "erro": "Acesso negado."
            }), 403

        if not usuario:
            return jsonify({
                "erro": "Usuário não encontrado"
            }), 404

        excluir_usuario(usuario)

        return jsonify({
            "mensagem": "Usuário removido com sucesso"
        }), 200

    except Exception as erro:
        return jsonify({
            "erro": str(erro)
        }), 500

@usuario_bp.route("/me", methods=["GET"])
@jwt_required()
def meu_perfil ():

    usuario_id = get_jwt_identity()

    usuario = Usuario.query.get(usuario_id)

    return jsonify(usuario.to_dict()), 200

@usuario_bp.route("/admin", methods=["GET"])
@jwt_required()
@admin_required
def painel_admin():

    usuario = buscar_usuario(usuario_id)


    if not usuario_id:
        return jsonify({
            "erro": "Email ou senha invalidos"
        }), 404


    return jsonify(usuario.to_dict()), 200