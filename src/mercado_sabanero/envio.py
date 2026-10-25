MUNICIPIO_BASE = "Sincelejo"
ENVIO_SINCELEJO = 8_000
ENVIO_OTROS_MUNICIPIOS = 15_000
BASE_ENVIO_GRATIS = 150_000


def calcular_envio(municipio, base=0, envio_gratis_por_cupon=False):
    if envio_gratis_por_cupon or base >= BASE_ENVIO_GRATIS:
        return 0
    if municipio == MUNICIPIO_BASE:
        return ENVIO_SINCELEJO
    return ENVIO_OTROS_MUNICIPIOS