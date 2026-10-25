MULTIPLICADOR_ORO = 2


def calcular_puntos(total_sin_envio, categoria="ESTANDAR"):
    puntos = total_sin_envio // 1_000
    if categoria == "ORO":
        return puntos * MULTIPLICADOR_ORO
    return puntos
