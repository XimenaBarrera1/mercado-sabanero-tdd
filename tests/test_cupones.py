from datetime import date
import pytest
from mercado_sabanero.cupones import calcular_descuento_cupon, cupon_da_envio_gratis


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

def test_enviogratis_da_envio_gratis():
    # Arrange
    codigo = "ENVIOGRATIS"
    # Act
    envio_gratis = cupon_da_envio_gratis(codigo)
    # Assert
    assert envio_gratis is True

def test_cupon_inexistente_lanza_error_de_cupon_invalido():
    # Arrange
    codigo = "XYZ"
    # Act y Assert
    with pytest.raises(ValueError, match="cupon invalido"):
        cupon_da_envio_gratis(codigo)

def test_cupon_vencido_lanza_error_de_cupon_invalido():
    # Arrange
    codigo = "ENVIOGRATIS"
    hoy = date(2099, 1, 1)
    # Act y Assert
    with pytest.raises(ValueError, match="cupon invalido"):
        cupon_da_envio_gratis(codigo, hoy)