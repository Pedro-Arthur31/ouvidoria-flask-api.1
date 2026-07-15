class StatusReclamacao:
    ABERTA = "Aberta"
    EM_ANDAMENTO = "Em_andamento"
    RESPONDIDA = "Respondida"
    FECHADA = "Fechada"


STATUS_VALIDOS = [
    StatusReclamacao.ABERTA,
    StatusReclamacao.EM_ANDAMENTO,
    StatusReclamacao.RESPONDIDA,
    StatusReclamacao.FECHADA
]