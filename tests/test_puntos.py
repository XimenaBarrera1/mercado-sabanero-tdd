from mercado_sabanero.puntos import calcular_puntos


def test_total_250515_acumula_250_puntos():
    # Arrange
    total_sin_envio = 250_515
    # Act
    puntos = calcular_puntos(total_sin_envio)
    # Assert
    assert puntos == 250
