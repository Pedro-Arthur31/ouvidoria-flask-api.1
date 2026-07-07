from utils.status import STATUS_VALIDOS


def validar_criacao_reclamacao(dados):

    titulo = dados.get("titulo")
    descricao = dados.get("descricao")

    if not titulo:
        raise ValueError(
            "Título é obrigatório."
        )

    if len(titulo.strip()) < 5:
        raise ValueError(
            "Título muito curto."
        )

    if len(titulo.strip()) > 150:
        raise ValueError(
            "Título muito grande."
        )

    if not descricao:
        raise ValueError(
            "Descrição obrigatória."
        )

    if len(descricao.strip()) < 15:
        raise ValueError(
            "Descrição muito pequena."
        )


def validar_atualizacao_reclamacao(dados):

    if "titulo" in dados:

        titulo = dados["titulo"]

        if not titulo.strip():
            raise ValueError("Título inválido.")

        if len(titulo.strip()) < 5:
            raise ValueError(
                "Título muito curto."
            )

    if "descricao" in dados:

        descricao = dados["descricao"]

        if not descricao.strip():
            raise ValueError(
                "Descrição inválida."
            )

        if len(descricao.strip()) < 15:
            raise ValueError(
                "Descrição muito pequena."
            )


def validar_status(status):

    if not status:
        raise ValueError(
            "Status obrigatório."
        )

    if status not in STATUS_VALIDOS:
        raise ValueError(
            "Status inválido."
        )