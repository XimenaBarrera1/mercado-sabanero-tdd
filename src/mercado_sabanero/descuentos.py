def calcular_descuento_volumen(subtotal):
    if subtotal >= 200_000:
        return (subtotal * 5 + 50) // 100
    return 0