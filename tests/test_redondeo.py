import pytest

from mercado_sabanero.redondeo import redondear


@pytest.mark.parametrize(
    "valor, esperado",
    [
        (0.5, 1),
        (1.5, 2),
        (2.5, 3),
        (2.4, 2),
    ],
)
def test_redondear_lleva_la_mitad_hacia_arriba(valor, esperado):
    # Arrange: valor y esperado vienen de parametrize
    # Act
    resultado = redondear(valor)
    # Assert
    assert resultado == esperado
