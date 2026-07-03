from flask import Blueprint, request, jsonify
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)

from extensions import db
from models.usuario import Usuario
from models.resposta import Resposta

resposta_bp = Blueprint('resposta', __name__)

@resposta_bp.route('/respostas', methods=['POST'])
@jwt_required()
def criar_resposta():
    usuario_id = get_jwt_identity()

    administrador = Usuario.query.get(usuario_id)

    if administrador.perfil != "administrador":
        return jsonify({
            "erro":"O usuario nao tem a permissao necessaria."
        }), 403

    dados = request.get_json()

    resposta = Resposta(
        mensagem=dados['mensagem'],
        administrador_id = usuario_id,
        reclamacao_id = dados['reclamacao_id'],
    )

    db.session.add(resposta)
    db.session.commit()

    return jsonify({
        "mensagem": "Resposta enviada com sucesso."
    }), 201