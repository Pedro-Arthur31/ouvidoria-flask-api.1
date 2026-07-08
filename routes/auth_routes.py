from flask import Blueprint, request, jsonify

from flask_jwt_extended import create_access_token

from werkzeug.security import check_password_hash

from models.usuario import Usuario

auth_bp = Blueprint(
    "auth",
    __name__
)


@auth_bp.route("/login", methods=["POST"])
def login():
    """ Login do usuário
    ---
    tags:
      - Autenticação

    consumes:
      - application/json

    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            email:
              type: string
              example: admin@email.com
            senha:
              type: string
              example: "123456"

    responses:
      200:
        description: Login realizado com sucesso

      400:
        description: Dados inválidos

      401:
        description: Email ou senha inválidos
    """
    dados = request.get_json()

    if not dados:
        return jsonify({
            "erro": "JSON não enviado."
        }), 400

    email = dados.get("email")
    senha = dados.get("senha")

    if not email:
        return jsonify({
            "erro": "Email é obrigatório."
        }), 400

    senha = str(senha)

    if not senha:
        return jsonify({
            "erro": "Senha é obrigatória."
        }), 400

    usuario = Usuario.query.filter_by(
        email=email
    ).first()

    if not usuario:
        return jsonify({
            "erro": "Email ou senha inválidos."
        }), 401

    if not check_password_hash(
        usuario.senha,
        senha
    ):
        return jsonify({
            "erro": "Email ou senha inválidos."
        }), 401

    token = create_access_token(
        identity=str(usuario.id),
        additional_claims={
            "perfil": usuario.perfil
        }
    )

    return jsonify({
        "access_token": token,
        "usuario": usuario.to_dict()
    }), 200
