UMBRAL_DESCUENTO_5 = 200_000
UMBRAL_DESCUENTO_10 = 500_000
PORCENTAJE_DESCUENTO_5 = 5
PORCENTAJE_DESCUENTO_10 = 10


def calcular_descuento_volumen(subtotal):
    if subtotal < 0:
        raise ValueError("El subtotal no puede ser negativo")
    if subtotal >= UMBRAL_DESCUENTO_10:
        return _porcentaje(subtotal, PORCENTAJE_DESCUENTO_10)
    if subtotal >= UMBRAL_DESCUENTO_5:
        return _porcentaje(subtotal, PORCENTAJE_DESCUENTO_5)
    return 0


def _porcentaje(valor, porcentaje):
    # Redondeo half-up con enteros: suma la mitad del divisor antes de dividir
    return (valor * porcentaje + 50) // 100