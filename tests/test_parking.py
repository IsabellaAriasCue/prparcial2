from src.parking import calcular_tarifa

def test_primeros_30_minutos_son_gratis():
    assert calcular_tarifa(0) == 0
    assert calcular_tarifa(30) == 0

def test_cobro_500_por_hora_o_fraccion_luego_de_30_min():
    assert calcular_tarifa(31) == 500
    assert calcular_tarifa(60) == 500
    assert calcular_tarifa(61) == 1000

def test_tope_maximo_diario_12000():
    assert calcular_tarifa(1440) == 12000 # 24 horas = (1410 min cobrables = 23.5h -> 24h cobradas = 12000)
    assert calcular_tarifa(2000) == 12000