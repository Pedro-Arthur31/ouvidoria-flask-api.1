from flask import Blueprint, request, jsonify

from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)

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