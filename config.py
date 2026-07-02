class Config:
    SQLALCHEMY_DATABASE_URI = (
        "mysql+pymysql://root:Ar@15009@localhost/ouvidoria_db"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = True