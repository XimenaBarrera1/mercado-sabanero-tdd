from decimal import Decimal

from mercado_sabanero.cupones import (
    CUPON_ENVIO_GRATIS,
    calcular_descuento_final,
)
from mercado_sabanero.envio import calcular_envio
from mercado_sabanero.iva import calcular_iva
from mercado_sabanero.puntos import calcular_puntos


def calcular_total(subtotal, descuento, iva, envio):
    return subtotal - descuento + iva + envio


def liquidar(carrito, municipio, categoria="ESTANDAR", codigo_cupon=None):
    if carrito.esta_vacio():
        raise ValueError("carrito vacio")

    lineas = carrito.lineas()
    subtotal = sum(producto.precio * cantidad for producto, cantidad in lineas)
    descuento = calcular_descuento_final(codigo_cupon, subtotal)
    porcentaje_descuento = Decimal(descuento) * 100 / Decimal(subtotal)

    iva = sum(
        calcular_iva(
            producto.precio * cantidad,
            producto.tarifa_iva,
            porcentaje_descuento,
        )
        for producto, cantidad in lineas
    )

    base = subtotal - descuento + iva
    envio = calcular_envio(
        municipio,
        base,
        envio_gratis_por_cupon=(codigo_cupon == CUPON_ENVIO_GRATIS),
    )
    total = calcular_total(subtotal, descuento, iva, envio)
    puntos = calcular_puntos(total - envio, categoria)

    return {
        "subtotal": subtotal,
        "descuento": descuento,
        "iva": iva,
        "envio": envio,
        "total": total,
        "puntos": puntos,
    }