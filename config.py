import os
from datetime import timedelta


class Config:
    database_url = os.getenv("DATABASE_URL")

    if database_url:
        database_url = database_url.replace(
            "mysql://",
            "mysql+pymysql://"
        )

        database_url = database_url.replace(
            "mysql+mysqldb://",
            "mysql+pymysql://"
        )

        database_url = database_url.replace(
            "ssl-mode=REQUIRED",
            "ssl=true"
        )

    SQLALCHEMY_DATABASE_URI = database_url

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=36)