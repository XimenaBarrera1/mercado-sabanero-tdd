from dataclasses import dataclass


@dataclass(frozen=True)
class Producto:
    id: str
    nombre: str
    precio: int
    tarifa_iva: int
