from mercado_sabanero.liquidacion import calcular_total


def test_total_es_subtotal_menos_descuento_mas_iva_mas_envio():
    # Arrange
    subtotal = 100_000
    descuento = 0
    iva = 19_000
    envio = 8_000
    # Act
    total = calcular_total(subtotal, descuento, iva, envio)
    # Assert
    assert total == 127_000

def test_total_resta_el_descuento_del_ejemplo_de_la_guia():
    # Arrange
    subtotal = 228_000
    descuento = 11_400
    iva = 33_915
    envio = 0
    # Act
    total = calcular_total(subtotal, descuento, iva, envio)
    # Assert
    assert total == 250_515