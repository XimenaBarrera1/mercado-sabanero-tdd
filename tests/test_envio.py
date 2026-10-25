from mercado_sabanero.envio import calcular_envio


def test_envio_dentro_de_sincelejo_cuesta_8000():
    # Arrange
    municipio = "Sincelejo"
    # Act
    envio = calcular_envio(municipio)
    # Assert
    assert envio == 8_000

def test_envio_a_otro_municipio_de_sucre_cuesta_15000():
    # Arrange
    municipio = "Corozal"
    # Act
    envio = calcular_envio(municipio)
    # Assert
    assert envio == 15_000