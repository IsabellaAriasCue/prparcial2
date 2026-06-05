import pytest
from src.parking import calcular_tarifa

def test_primeros_30_minutos_son_gratis():
    assert calcular_tarifa(0) == 0
    assert calcular_tarifa(30) == 0