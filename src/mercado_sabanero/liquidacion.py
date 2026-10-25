from decimal import Decimal

from mercado_sabanero.cupones import (
    CUPON_ENVIO_GRATIS,
    calcular_descuento_final,
)
from mercado_sabanero.envio import calcular_envio
from mercado_sabanero.iva import calcular_iva
from mercado_sabanero.puntos import calcular_puntos

MENSAJE_CARRITO_VACIO = "carrito vacio"


def calcular_total(subtotal, descuento, iva, envio):
    return subtotal - descuento + iva + envio


def _calcular_iva_total(lineas, porcentaje_descuento):
    return sum(
        calcular_iva(
            producto.precio * cantidad,
            producto.tarifa_iva,
            porcentaje_descuento,
        )
        for producto, cantidad in lineas
    )


def liquidar(carrito, municipio, categoria="ESTANDAR", codigo_cupon=None):
    if carrito.esta_vacio():
        raise ValueError(MENSAJE_CARRITO_VACIO)

    lineas = carrito.lineas()
    subtotal = sum(producto.precio * cantidad for producto, cantidad in lineas)
    descuento = calcular_descuento_final(codigo_cupon, subtotal)
    porcentaje_descuento = Decimal(descuento) * 100 / Decimal(subtotal)
    iva = _calcular_iva_total(lineas, porcentaje_descuento)

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