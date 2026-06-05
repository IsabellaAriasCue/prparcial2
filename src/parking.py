import math


def calcular_tarifa(minutos: int) -> float:
    if minutos <= 30:
        return 0

    # Las horas o fracciones se calculan sobre el tiempo TOTAL de estadía
    horas = math.ceil(minutos / 60)
    return horas * 500