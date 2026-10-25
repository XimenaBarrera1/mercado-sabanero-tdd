from unittest.mock import Mock

import pytest

from mercado_sabanero.carrito import Carrito
from mercado_sabanero.errores import CantidadInvalidaError, StockInsuficienteError
from mercado_sabanero.producto import Producto


def test_agregar_1_unidad_con_stock_suficiente_queda_en_el_carrito():
    # Arrange
    inventario = Mock()
    inventario.stock_disponible.return_value = 10
    producto = Producto(id="LIC-01", nombre="Licuadora", precio=180_000, tarifa_iva=19)
    carrito = Carrito(inventario)
    # Act
    carrito.agregar(producto, 1)
    # Assert
    assert carrito.cantidad_de(producto) == 1


@pytest.mark.parametrize("cantidad", [0, 51, -1])
def test_agregar_cantidad_fuera_de_rango_lanza_error(cantidad):
    # Arrange
    inventario = Mock()
    inventario.stock_disponible.return_value = 100
    producto = Producto(id="LIC-01", nombre="Licuadora", precio=180_000, tarifa_iva=19)
    carrito = Carrito(inventario)
    # Act y Assert
    with pytest.raises(CantidadInvalidaError):
        carrito.agregar(producto, cantidad)



def test_agregar_mas_unidades_que_el_stock_lanza_error_de_stock_insuficiente():
    # Arrange
    inventario = Mock()
    inventario.stock_disponible.return_value = 5
    producto = Producto(id="LIC-01", nombre="Licuadora", precio=180_000, tarifa_iva=19)
    carrito = Carrito(inventario)
    # Act y Assert
    with pytest.raises(StockInsuficienteError):
        carrito.agregar(producto, 10)


def test_agregar_el_mismo_producto_dos_veces_suma_las_cantidades():
    # Arrange
    inventario = Mock()
    inventario.stock_disponible.return_value = 10
    producto = Producto(id="LIC-01", nombre="Licuadora", precio=180_000, tarifa_iva=19)
    carrito = Carrito(inventario)
    carrito.agregar(producto, 2)
    # Act
    carrito.agregar(producto, 3)
    # Assert
    assert carrito.cantidad_de(producto) == 5


@pytest.mark.parametrize("cantidad", [1, 25, 50])
def test_agregar_cantidad_valida_queda_la_cantidad_pedida(cantidad):
    # Arrange
    inventario = Mock()
    inventario.stock_disponible.return_value = 100
    producto = Producto(id="LIC-01", nombre="Licuadora", precio=180_000, tarifa_iva=19)
    carrito = Carrito(inventario)
    # Act
    carrito.agregar(producto, cantidad)
    # Assert
    assert carrito.cantidad_de(producto) == cantidad


def test_agregar_consulta_el_inventario_una_vez_con_el_id_del_producto():
    # Arrange
    inventario = Mock()
    inventario.stock_disponible.return_value = 10
    producto = Producto(id="LIC-01", nombre="Licuadora", precio=180_000, tarifa_iva=19)
    carrito = Carrito(inventario)
    # Act
    carrito.agregar(producto, 1)
    # Assert
    inventario.stock_disponible.assert_called_once_with("LIC-01")
