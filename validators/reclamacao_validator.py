from utils.status import STATUS_VALIDOS


def validar_criacao_reclamacao(dados):

    titulo = dados.get("titulo")
    descricao = dados.get("descricao")

    if not titulo:
        raise ValueError("O título é obrigatório.")

    if len(titulo.strip()) < 5:
        raise ValueError("O título deve possuir pelo menos 5 caracteres.")

    if len(titulo.strip()) > 150:
        raise ValueError("O título deve possuir no máximo 150 caracteres.")

    if not descricao:
        raise ValueError("A descrição é obrigatória.")

    if len(descricao.strip()) < 15:
        raise ValueError("A descrição deve possuir pelo menos 15 caracteres.")


def validar_atualizacao_reclamacao(dados):

    if "titulo" in dados:

        titulo = dados["titulo"]

        if not titulo.strip():
            raise ValueError("O título não pode ficar vazio.")

        if len(titulo.strip()) < 5:
            raise ValueError("O título deve possuir pelo menos 5 caracteres.")

        if len(titulo.strip()) > 150:
            raise ValueError("O título deve possuir no máximo 150 caracteres.")

    if "descricao" in dados:

        descricao = dados["descricao"]

        if not descricao.strip():
            raise ValueError("A descrição não pode ficar vazia.")

        if len(descricao.strip()) < 15:
            raise ValueError("A descrição deve possuir pelo menos 15 caracteres.")


def validar_status(status):

    if not status:
        raise ValueError("O status é obrigatório.")

    if status not in STATUS_VALIDOS:
        raise ValueError(
            f"Status inválido. Status permitidos: {', '.join(STATUS_VALIDOS)}"
        )