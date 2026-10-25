class CantidadInvalidaError(ValueError):
    """La cantidad pedida está fuera del rango permitido (1 a 50)."""


class StockInsuficienteError(Exception):
    """El stock disponible es menor que la cantidad pedida."""
