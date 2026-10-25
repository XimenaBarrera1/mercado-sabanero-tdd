from unittest.mock import Mock

from mercado_sabanero.carrito import Carrito
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
