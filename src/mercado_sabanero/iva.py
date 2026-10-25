from decimal import Decimal

from mercado_sabanero.redondeo import redondear


def calcular_iva(valor, tarifa_iva):
    return redondear(Decimal(valor) * tarifa_iva / 100)
