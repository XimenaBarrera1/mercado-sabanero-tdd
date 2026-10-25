from decimal import Decimal

from mercado_sabanero.redondeo import redondear


def calcular_iva(valor, tarifa_iva, porcentaje_descuento=0):
    valor_con_descuento = Decimal(valor) * (100 - porcentaje_descuento) / 100
    return redondear(valor_con_descuento * tarifa_iva / 100)
