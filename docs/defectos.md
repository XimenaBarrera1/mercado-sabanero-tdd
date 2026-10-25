# Registro de defectos

| ID | Descripción | Pasos para reproducir | Severidad | Estado |
|---|---|---|---|---|
| DEF-01 | El carrito no valida el límite de 50 unidades ni el stock sobre la cantidad acumulada del producto. Solo valida cada llamada a `agregar()` por separado. | 1. Crear un carrito con inventario de stock 100. 2. Agregar 30 unidades de un producto. 3. Agregar otras 30 del mismo producto. 4. El carrito queda con 60 unidades, más que el límite de 50. | Media | Abierto |
