from datetime import timedelta
from app import app

class Config:

    # ==========================
    # Banco de Dados
    # ==========================

    import os

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
        "DATABASE_URL"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # ==========================
    # JWT
    # ==========================

    JWT_SECRET_KEY = "minha_chave_de_api_julia"

    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=365)