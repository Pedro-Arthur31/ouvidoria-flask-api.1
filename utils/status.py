class StatusReclamacao:
    ABERTA = "aberta"
    EM_ANDAMENTO = "em_andamento"
    RESPONDIDA = "respondida"
    FECHADA = "fechada"


STATUS_VALIDOS = [
    StatusReclamacao.ABERTA,
    StatusReclamacao.EM_ANDAMENTO,
    StatusReclamacao.RESPONDIDA,
    StatusReclamacao.FECHADA
]