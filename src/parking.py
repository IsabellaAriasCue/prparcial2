import math

def calcular_tarifa(minutos: int, es_vip: bool = False) -> float:
    if minutos <= 30:
        return 0

    # Las horas o fracciones se calculan sobre el total de minutos
    horas = math.ceil(minutos / 60)
    total = horas * 500

    return min(total, 12000)
