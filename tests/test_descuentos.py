from mercado_sabanero.descuentos import calcular_descuento_volumen


def test_subtotal_199999_no_aplica_descuento():
    # Arrange
    subtotal = 199_999
    # Act
    descuento = calcular_descuento_volumen(subtotal)
    # Assert
    assert descuento == 0