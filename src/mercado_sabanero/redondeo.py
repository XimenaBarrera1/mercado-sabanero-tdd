from decimal import Decimal, ROUND_HALF_UP

UN_PESO = Decimal("1")


def redondear(valor):
    """Redondea al peso más cercano; las mitades suben (2,5 -> 3)."""
    return int(Decimal(str(valor)).quantize(UN_PESO, rounding=ROUND_HALF_UP))
