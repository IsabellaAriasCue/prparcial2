# Diseño de Pruebas: ParkingUV S.A.S.

## Regla 1: Primeros 30 minutos gratuitos
* **Particiones de Equivalencia:** * Clase Válida 1: <= 30 min (Costo: $0)
    * Clase Válida 2: > 30 min (Costo: > $0)
* **Valores Límite:** 0 min, 30 min ($0), 31 min ($500).

## Regla 2: Tope máximo de $12.000 por día (24 horas / 1440 min)
* **Particiones de Equivalencia:**
    * Clase Válida 1: Cobro acumulado < $12.000
    * Clase Válida 2: Cobro acumulado >= $12.000 (Tope: $12.000)
* **Valores Límite (sabiendo que $500/hr llega a 12000 a las 24.5h):** * 1410 min (23h 30m) = $11.500
    * 1470 min (24h 30m) = $12.000 (Aplica tope)