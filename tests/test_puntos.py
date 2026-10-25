import pytest

from mercado_sabanero.puntos import calcular_puntos


def test_total_250515_acumula_250_puntos():
    # Arrange
    total_sin_envio = 250_515
    # Act
    puntos = calcular_puntos(total_sin_envio)
    # Assert
    assert puntos == 250


@pytest.mark.parametrize(
    "total_sin_envio, puntos_esperados",
    [
        (0, 0),
        (999, 0),
        (1_000, 1),
        (1_999, 1),
        (2_000, 2),
    ],
)
def test_limites_de_puntos_por_cada_mil_pesos_completos(total_sin_envio, puntos_esperados):
    # Arrange: los datos llegan por parametrize
    # Act
    puntos = calcular_puntos(total_sin_envio)
    # Assert
    assert puntos == puntos_esperados



def test_cliente_oro_recibe_el_doble_de_puntos():
    # Arrange
    total_sin_envio = 250_515
    categoria = "ORO"
    # Act
    puntos = calcular_puntos(total_sin_envio, categoria=categoria)
    # Assert
    assert puntos == 500


def test_el_envio_no_suma_puntos():
    # Arrange
    total_con_envio = 127_000
    envio = 8_000
    total_sin_envio = total_con_envio - envio
    # Act
    puntos = calcular_puntos(total_sin_envio)
    # Assert
    assert puntos == 119

