from mercado_sabanero.errores import CantidadInvalidaError


class Carrito:
    def __init__(self, inventario):
        self._inventario = inventario
        self._items = {}

    def agregar(self, producto, cantidad):
        if cantidad < 1 or cantidad > 50:
            raise CantidadInvalidaError(
                f"La cantidad debe estar entre 1 y 50, se recibió {cantidad}"
            )
        self._items[producto.id] = cantidad

    def cantidad_de(self, producto):
        return self._items[producto.id]
