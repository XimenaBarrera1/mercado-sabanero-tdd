def calcular_descuento_cupon(codigo, subtotal):
    if subtotal < 50_000:
        raise ValueError("El subtotal no alcanza el minimo del cupon")
    return 5_000

def cupon_da_envio_gratis(codigo):
    if codigo != "ENVIOGRATIS":
        raise ValueError("cupon invalido")
    return True