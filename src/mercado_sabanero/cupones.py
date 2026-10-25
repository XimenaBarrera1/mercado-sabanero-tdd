from datetime import date

FECHA_VENCIMIENTO_ENVIOGRATIS = date(2026, 12, 31)

def calcular_descuento_cupon(codigo, subtotal):
    if subtotal < 50_000:
        raise ValueError("El subtotal no alcanza el minimo del cupon")
    return 5_000

def cupon_da_envio_gratis(codigo, hoy=None):
    if codigo != "ENVIOGRATIS":
        raise ValueError("cupon invalido")
    if hoy is not None and hoy > FECHA_VENCIMIENTO_ENVIOGRATIS:
        raise ValueError("cupon invalido")
    return True