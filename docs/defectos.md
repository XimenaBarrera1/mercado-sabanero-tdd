# Registro de defectos

| ID | Descripción | Pasos para reproducir | Severidad | Estado |
|---|---|---|---|---|
| DEF-01 | El carrito no valida el límite de 50 unidades ni el stock sobre la cantidad acumulada del producto. Solo valida cada llamada a `agregar()` por separado. | 1. Crear un carrito con inventario de stock 100. 2. Agregar 30 unidades de un producto. 3. Agregar otras 30 del mismo producto. 4. El carrito queda con 60 unidades, más que el límite de 50. | Media | Abierto |
| DEF-02 | `calcular_descuento_final` lanza `ValueError: cupon invalido` cuando no hay cupón (`None`) o cuando el cupón es ENVIOGRATIS, aunque la compra sea válida. La compra de I-01 es sin cupón y se rompería al integrar. | 1. Estar en la rama `feat/hu-04-cupones`. 2. Ejecutar `calcular_descuento_final(None, 228000)`. 3. Se lanza `ValueError: cupon invalido` en lugar de devolver el descuento por volumen de 11.400. | Alta | Abierto (reportado a Lizeth en el PR #5) |
