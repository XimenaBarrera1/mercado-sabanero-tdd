import pytest
from mercado_sabanero.descuentos import calcular_descuento_volumen


def test_subtotal_199999_no_aplica_descuento():
    # Arrange
    subtotal = 199_999
    # Act
    descuento = calcular_descuento_volumen(subtotal)
    # Assert
    assert descuento == 0

def test_subtotal_200000_aplica_descuento_5_porciento():
    # Arrange
    subtotal = 200_000
    # Act
    descuento = calcular_descuento_volumen(subtotal)
    # Assert
    assert descuento == 10_000

def test_subtotal_499999_redondea_descuento_al_peso_mas_cercano():
    # Arrange
    subtotal = 499_999
    # Act
    descuento = calcular_descuento_volumen(subtotal)
    # Assert
    assert descuento == 25_000

def test_subtotal_500000_aplica_descuento_10_porciento():
    # Arrange
    subtotal = 500_000
    # Act
    descuento = calcular_descuento_volumen(subtotal)
    # Assert
    assert descuento == 50_000

def test_subtotal_negativo_lanza_error():
    # Arrange
    subtotal = -1
    # Act y Assert
    with pytest.raises(ValueError):
        calcular_descuento_volumen(subtotal)