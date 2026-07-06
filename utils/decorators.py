from functools import wraps
from flask import jsonify
from models.usuario import Usuario
from flask_jwt_extended import verify_jwt_in_request, get_jwt


def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()

        claims = get_jwt()

        if claims.get("tipo") != "admin":
            return {"erro": "Apenas administradores podem acessar."}, 403

        return fn(*args, **kwargs)

    return wrapper