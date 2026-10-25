from decimal import Decimal, ROUND_HALF_UP


def redondear(valor):
    return int(Decimal(str(valor)).quantize(Decimal("1"), rounding=ROUND_HALF_UP))
