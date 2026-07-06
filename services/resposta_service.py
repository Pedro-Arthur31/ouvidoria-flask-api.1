def validar_criacao_resposta(dados):

    mensagem = dados.get("mensagem")

    if not mensagem:
        raise ValueError("A mensagem é obrigatória.")

    if len(mensagem.strip()) < 5:
        raise ValueError(
            "A resposta deve possuir pelo menos 5 caracteres."
        )

    if "reclamacao_id" not in dados:
        raise ValueError("O ID da reclamação é obrigatório.")


def validar_atualizacao_resposta(dados):

    if "mensagem" in dados:

        mensagem = dados["mensagem"]

        if not mensagem.strip():
            raise ValueError("A mensagem não pode ficar vazia.")

        if len(mensagem.strip()) < 5:
            raise ValueError(
                "A resposta deve possuir pelo menos 5 caracteres."
            )