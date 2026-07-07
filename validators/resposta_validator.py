def validar_criacao_resposta(dados):

    mensagem = dados.get("mensagem")
    reclamacao_id = dados.get("reclamacao_id")

    if not mensagem:
        raise ValueError(
            "Mensagem obrigatória."
        )

    if len(mensagem.strip()) < 5:
        raise ValueError(
            "Mensagem muito pequena."
        )

    if not reclamacao_id:
        raise ValueError(
            "Reclamação obrigatória."
        )


def validar_atualizacao_resposta(dados):

    if "mensagem" in dados:

        mensagem = dados["mensagem"]

        if not mensagem.strip():
            raise ValueError(
                "Mensagem inválida."
            )

        if len(mensagem.strip()) < 5:
            raise ValueError(
                "Mensagem muito pequena."
            )