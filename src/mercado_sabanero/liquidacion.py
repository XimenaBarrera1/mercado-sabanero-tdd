def calcular_total(subtotal, descuento, iva, envio):
    return subtotal - descuento + iva + envio

def liquidar(carrito):
    if carrito.esta_vacio():
        raise ValueError("carrito vacio")