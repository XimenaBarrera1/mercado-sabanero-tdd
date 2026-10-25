from mercado_sabanero.redondeo import redondear


def test_redondear_2_5_devuelve_3():
    # Arrange
    valor = 2.5
    # Act
    resultado = redondear(valor)
    # Assert
    assert resultado == 3
