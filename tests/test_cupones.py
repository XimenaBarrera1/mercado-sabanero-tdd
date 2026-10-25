import pytest
from mercado_sabanero.cupones import calcular_descuento_cupon


def test_sabanero10_con_subtotal_50000_da_descuento_10_porciento():
    # Arrange
    codigo = "SABANERO10"
    subtotal = 50_000
    # Act
    descuento = calcular_descuento_cupon(codigo, subtotal)
    # Assert
    assert descuento == 5_000

def test_sabanero10_bajo_el_minimo_lanza_error():
    # Arrange
    codigo = "SABANERO10"
    subtotal = 49_999
    # Act y Assert
    with pytest.raises(ValueError):
        calcular_descuento_cupon(codigo, subtotal)