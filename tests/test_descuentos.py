import pytest
from mercado_sabanero.descuentos import calcular_descuento_volumen


@pytest.mark.parametrize(
    "subtotal, descuento_esperado",
    [
        (199_999, 0),
        (200_000, 10_000),
        (499_999, 25_000),
        (500_000, 50_000),
    ],
)
def test_limites_del_descuento_por_volumen(subtotal, descuento_esperado):
    # Arrange: los datos llegan por parametrize
    # Act
    descuento = calcular_descuento_volumen(subtotal)
    # Assert
    assert descuento == descuento_esperado


def test_subtotal_negativo_lanza_error():
    # Arrange
    subtotal = -1
    # Act y Assert
    with pytest.raises(ValueError):
        calcular_descuento_volumen(subtotal)