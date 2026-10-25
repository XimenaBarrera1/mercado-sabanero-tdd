import pytest

from mercado_sabanero.iva import calcular_iva


@pytest.mark.parametrize(
    "tarifa, iva_esperado",
    [
        (0, 0),
        (5, 5_000),
        (19, 19_000),
    ],
)
def test_iva_segun_tarifa_sobre_100000(tarifa, iva_esperado):
    # Arrange
    valor = 100_000
    # Act
    iva = calcular_iva(valor, tarifa)
    # Assert
    assert iva == iva_esperado


def test_iva_se_calcula_sobre_el_valor_con_descuento_aplicado():
    # Arrange
    valor = 180_000
    tarifa = 19
    porcentaje_descuento = 5
    # Act
    iva = calcular_iva(valor, tarifa, porcentaje_descuento)
    # Assert
    assert iva == 32_490


def test_iva_con_decimales_se_redondea_al_peso_mas_cercano():
    # Arrange
    valor = 1_010
    tarifa = 5
    # Act
    iva = calcular_iva(valor, tarifa)
    # Assert
    assert iva == 51
