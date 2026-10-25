# Registro de defectos

| ID | Descripción | Pasos para reproducir | Severidad | Estado |
|---|---|---|---|---|
| DEF-01 | El carrito no valida el límite de 50 unidades ni el stock sobre la cantidad acumulada del producto. Solo valida cada llamada a `agregar()` por separado. | 1. Crear un carrito con inventario de stock 100. 2. Agregar 30 unidades de un producto. 3. Agregar otras 30 del mismo producto. 4. El carrito queda con 60 unidades, más que el límite de 50. | Media | Abierto |

| ID | Descripción | Pasos para reproducir | Severidad | Estado |
|---|---|---|---|---|
| DEF-02 | calcular_descuento_cupon devolvía 5.000 fijo sin importar el subtotal | calcular_descuento_cupon("SABANERO10", 300_000) daba 5.000 en vez de 30.000 | Alta (afecta dinero) | Cerrado |


| ID | Descripción | Pasos para reproducir | Severidad | Estado |
|---|---|---|---|---|
| DEF-03 | calcular_descuento_final lanzaba cupon invalido cuando no había cupón (None) | calcular_descuento_final(None, 228_000)| Alta (bloquea toda compra sin cupón) | Cerrado |
