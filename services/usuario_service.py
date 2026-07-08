from werkzeug.security import generate_password_hash

from extensions import db
from models.usuario import Usuario


def criar_usuario(nome, email, senha):
    senha = str(senha)
    usuario = Usuario(
        nome=nome,
        email=email,
        senha=generate_password_hash(senha)
    )

    db.session.add(usuario)
    db.session.commit()

    return usuario


def listar_usuarios():

    return Usuario.query.all()


def buscar_usuario(id):

    usuario = Usuario.query.get(id)

    if not usuario:
        raise ValueError("Usuário não encontrado.")

    return usuario


def atualizar_usuario(usuario, dados):

    if "nome" in dados:
        usuario.nome = dados["nome"]

    if "email" in dados:
        usuario.email = dados["email"]

    if "senha" in dados:
        usuario.senha = generate_password_hash(
            dados["senha"]
        )

    db.session.commit()

    return usuario


def excluir_usuario(usuario):

    db.session.delete(usuario)

    db.session.commit()