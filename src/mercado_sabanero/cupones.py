from datetime import date

from decimal import Decimal

from mercado_sabanero.redondeo import redondear

from mercado_sabanero.descuentos import calcular_descuento_volumen

FECHA_VENCIMIENTO_ENVIOGRATIS = date(2026, 12, 31)

def calcular_descuento_cupon(codigo, subtotal):
    if subtotal < 50_000:
        raise ValueError("El subtotal no alcanza el minimo del cupon")
    return redondear(Decimal(subtotal) * 10 / 100)

def cupon_da_envio_gratis(codigo, hoy=None):
    if codigo != "ENVIOGRATIS":
        raise ValueError("cupon invalido")
    if hoy is not None and hoy > FECHA_VENCIMIENTO_ENVIOGRATIS:
        raise ValueError("cupon invalido")
    return True

def calcular_descuento_final(codigo, subtotal):
    descuento_volumen = calcular_descuento_volumen(subtotal)
    descuento_cupon = calcular_descuento_cupon(codigo, subtotal)
    return max(descuento_volumen, descuento_cupon)