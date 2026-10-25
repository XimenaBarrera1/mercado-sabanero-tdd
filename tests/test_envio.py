from mercado_sabanero.envio import calcular_envio


def test_envio_dentro_de_sincelejo_cuesta_8000():
    # Arrange
    municipio = "Sincelejo"
    # Act
    envio = calcular_envio(municipio)
    # Assert
    assert envio == 8_000