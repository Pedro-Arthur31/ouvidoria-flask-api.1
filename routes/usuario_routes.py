from flask import Blueprint, request, jsonify
from extensions import db
from models.usuario import Usuario
from werkzeug.security import generate_password_hash
from flask_jwt_extended import jwt_required, get_jwt_identity


usuario_bp = Blueprint("usuario", __name__)

@usuario_bp.route("/usuarios", methods=["POST"])
def criar_usuario():
    try:
        dados = request.json

        senha_hash = generate_password_hash(dados["senha"])
        novo_usuario = Usuario(
            nome=dados["nome"],
            email=dados["email"],
            senha=senha_hash
        )

        db.session.add(novo_usuario)
        db.session.commit()

        return jsonify({
            "mensagem": "Usuário criado com sucesso"
        }), 201

    except Exception as erro:
        return jsonify({
            "erro": str(erro)
        }), 500

@usuario_bp.route("/usuarios", methods=["GET"])
@jwt_required()
def listar_usuarios():
    try:
        usuarios = Usuario.query.all()

        lista = []

        for usuario in usuarios:
            lista.append({
                "id": usuario.id,
                "nome": usuario.nome,
                "email": usuario.email,
                "perfil": usuario.perfil
            })

        return jsonify(lista), 200
    except Exception as erro:
        return jsonify({
            "erro": str(erro)
        }), 500

@usuario_bp.route("/usuarios/<int:id>", methods=["GET"])
def buscar_usuario(id):
    try:
        usuario = Usuario.query.get(id)
        if not usuario:
            return jsonify({
                "erro": "Usuário não encontrado"
            }), 404
        return jsonify({
            "id": usuario.id,
            "nome": usuario.nome,
            "email": usuario.email,
            "perfil": usuario.perfil
        }),200
    except Exception as erro:
        return jsonify({
            "erro": str(erro)
        }),500
@usuario_bp.route("/usuarios/<int:id>", methods=["PUT"])
def atualizar_usuario(id):
    try:
        usuario = Usuario.query.get(id)

        if not usuario:
            return jsonify({
                "erro": "Usuário não encontrado"
            }), 404

        dados = request.json

        usuario.nome = dados.get(
            "nome",
            usuario.nome
        )

        usuario.email = dados.get(
            "email",
            usuario.email
        )

        usuario.senha = dados.get(
            "senha",
            usuario.senha
        )

        db.session.commit()

        return jsonify({
            "mensagem": "Usuário atualizado com sucesso"
        }), 200

    except Exception as erro:
        return jsonify({
            "erro": str(erro)
        }), 500
@usuario_bp.route("/usuarios/<int:id>", methods=["DELETE"])
def deletar_usuario(id):
    try:
        usuario = Usuario.query.get(id)

        if not usuario:
            return jsonify({
                "erro": "Usuário não encontrado"
            }), 404

        db.session.delete(usuario)
        db.session.commit()

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

    return jsonify({
        "id": usuario.id,
        "nome": usuario.nome,
        "email": usuario.email,
        "perfil": usuario.perfil
    }), 200

@usuario_bp.route("/admin", methods=["GET"])
@jwt_required()
def painel_admin():

    usuario_id = get_jwt_identity()

    usuario = Usuario.query.get(usuario_id)

    if not usuario:
        return jsonify({
            "erro": "Email ou senha invalidos"
        }), 404

    if usuario.perfil != "administrador":
        return jsonify({
            "erro": f"Acesso negado. Apenas administradores podem acessar."
        }), 403
    return jsonify({
        "mensagem": f"Bem-vindo ao painel administrativo. {usuario.nome}!",
        "usuario": {
            "id": usuario.id,
            "nome": usuario.nome,
            "email": usuario.email,
            "perfil": usuario.perfil
        }
    }), 200