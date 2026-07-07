from datetime import timedelta


class Config:

    # ==========================
    # Banco de Dados
    # ==========================

    SQLALCHEMY_DATABASE_URI = (
        "mysql+pymysql://root:root@localhost/ouvidoria_db"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # ==========================
    # JWT
    # ==========================

    JWT_SECRET_KEY = "minha_chave_de_api_julia"

    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)