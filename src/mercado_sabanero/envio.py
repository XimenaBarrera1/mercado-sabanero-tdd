def calcular_envio(municipio, base=0):
    if base >= 150_000:
        return 0
    if municipio == "Sincelejo":
        return 8_000
    return 15_000