from extensions import db
from models.usuario import Usuario
from werkzeug.security import generate_password_hash

def buscar_usuario(id):

    return Usuario.query.get(id)

def listar_usuarios():
    return Usuario.query.all()

def excluir_usuario(usuario):

    db.session.delete(usuario)

    db.session.commit()

def criar_usuario(nome, email, senha):

    usuario_existente = Usuario.query.filter_by(
        email=email
    ).first()

    if usuario_existente:
        raise ValueError("Email já cadastrado.")

    senha_hash = generate_password_hash(senha)

    usuario = Usuario(
        nome=nome,
        email=email,
        senha=senha_hash
    )

    db.session.add(usuario)

    db.session.commit()

    return usuario

def atualizar_usuario(usuario, dados):

    usuario.nome = dados.get(
        "nome",
        usuario.nome
    )

    usuario.email = dados.get(
        "email",
        usuario.email
    )

    if "senha" in dados:

        usuario.senha = generate_password_hash(
            dados["senha"]
        )

    db.session.commit()

    return usuario
