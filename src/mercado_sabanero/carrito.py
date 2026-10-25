from mercado_sabanero.errores import CantidadInvalidaError, StockInsuficienteError


class Carrito:
    def __init__(self, inventario):
        self._inventario = inventario
        self._items = {}

    def agregar(self, producto, cantidad):
        if cantidad < 1 or cantidad > 50:
            raise CantidadInvalidaError(
                f"La cantidad debe estar entre 1 y 50, se recibió {cantidad}"
            )
        stock = self._inventario.stock_disponible(producto.id)
        if stock < cantidad:
            raise StockInsuficienteError(
                f"Stock insuficiente: se pidieron {cantidad} y hay {stock}"
            )
        self._items[producto.id] = self._items.get(producto.id, 0) + cantidad

    def cantidad_de(self, producto):
        return self._items[producto.id]

