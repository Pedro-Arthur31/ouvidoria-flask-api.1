from models.usuario import Usuario


def validar_criacao_usuario(dados):

    nome = dados.get("nome")
    email = dados.get("email")
    senha = dados.get("senha")

    if not nome:
        raise ValueError("Nome é obrigatório.")

    if len(nome.strip()) < 3:
        raise ValueError("Nome deve possuir pelo menos 3 caracteres.")

    if not email:
        raise ValueError("Email é obrigatório.")

    if "@" not in email:
        raise ValueError("Email inválido.")

    usuario = Usuario.query.filter_by(
        email=email
    ).first()

    if usuario:
        raise ValueError("Email já cadastrado.")

    if not senha:
        raise ValueError("Senha é obrigatória.")

    if len(senha) < 6:
        raise ValueError("Senha deve possuir pelo menos 6 caracteres.")


def validar_atualizacao_usuario(dados):

    if "nome" in dados:

        nome = dados["nome"]

        if not nome.strip():
            raise ValueError("Nome inválido.")

        if len(nome.strip()) < 3:
            raise ValueError(
                "Nome muito curto."
            )

    if "email" in dados:

        email = dados["email"]

        if not email.strip():
            raise ValueError("Email inválido.")

        if "@" not in email:
            raise ValueError("Email inválido.")

    if "senha" in dados:

        senha = dados["senha"]

        if len(senha) < 6:
            raise ValueError(
                "Senha deve possuir pelo menos 6 caracteres."
            )