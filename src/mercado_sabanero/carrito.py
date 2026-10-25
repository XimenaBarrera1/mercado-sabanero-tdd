class Carrito:
    def __init__(self, inventario):
        self._inventario = inventario
        self._items = {}

    def agregar(self, producto, cantidad):
        self._items[producto.id] = cantidad

    def cantidad_de(self, producto):
        return self._items[producto.id]
