from decimal import Decimal

from mercado_sabanero.redondeo import redondear

TARIFAS_VALIDAS = (0, 5, 19)


def calcular_iva(valor, tarifa_iva, porcentaje_descuento=0):
    if valor < 0:
        raise ValueError(f"El valor no puede ser negativo: {valor}")
    if tarifa_iva not in TARIFAS_VALIDAS:
        raise ValueError(f"Tarifa de IVA inválida: {tarifa_iva}. Debe ser 0, 5 o 19")
    valor_con_descuento = Decimal(valor) * (100 - porcentaje_descuento) / 100
    return redondear(valor_con_descuento * tarifa_iva / 100)
