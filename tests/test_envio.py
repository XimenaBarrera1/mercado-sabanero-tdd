import pytest

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

@pytest.mark.parametrize(
    "base, envio_esperado",
    [
        (149_999, 8_000),
        (150_000, 0),
    ],
)
def test_envio_gratis_desde_150000_de_base(base, envio_esperado):
    # Arrange
    municipio = "Sincelejo"
    # Act
    envio = calcular_envio(municipio, base)
    # Assert
    assert envio == envio_esperado

def test_cupon_envio_gratis_da_envio_cero_con_base_menor_a_150000():
    # Arrange
    municipio = "Sincelejo"
    base = 119_000
    # Act
    envio = calcular_envio(municipio, base, envio_gratis_por_cupon=True)
    # Assert
    assert envio == 0