from unittest.mock import Mock

import pytest

from mercado_sabanero.carrito import Carrito
from mercado_sabanero.liquidacion import calcular_total, liquidar
from mercado_sabanero.producto import Producto

def test_total_es_subtotal_menos_descuento_mas_iva_mas_envio():
    # Arrange
    subtotal = 100_000
    descuento = 0
    iva = 19_000
    envio = 8_000
    # Act
    total = calcular_total(subtotal, descuento, iva, envio)
    # Assert
    assert total == 127_000

def test_total_resta_el_descuento_del_ejemplo_de_la_guia():
    # Arrange
    subtotal = 228_000
    descuento = 11_400
    iva = 33_915
    envio = 0
    # Act
    total = calcular_total(subtotal, descuento, iva, envio)
    # Assert
    assert total == 250_515

def test_liquidar_carrito_vacio_lanza_error():
    # Arrange
    carrito = Carrito(Mock())
    # Act y Assert
    with pytest.raises(ValueError, match="carrito vacio"):
        liquidar(carrito)

def test_liquidar_el_ejemplo_de_la_guia_da_total_250515_y_250_puntos():
    # Arrange
    inventario = Mock()
    inventario.stock_disponible.return_value = 100
    licuadora = Producto(id="LIC-01", nombre="Licuadora", precio=180_000, tarifa_iva=19)
    cafe = Producto(id="CAF-01", nombre="Cafe", precio=15_000, tarifa_iva=5)
    arroz = Producto(id="ARR-01", nombre="Arroz", precio=4_500, tarifa_iva=0)
    carrito = Carrito(inventario)
    carrito.agregar(licuadora, 1)
    carrito.agregar(cafe, 2)
    carrito.agregar(arroz, 4)
    # Act
    resultado = liquidar(carrito, "Sincelejo")
    # Assert
    assert resultado == {
        "subtotal": 228_000,
        "descuento": 11_400,
        "iva": 33_915,
        "envio": 0,
        "total": 250_515,
        "puntos": 250,
    }