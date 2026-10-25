# Mercado Sabanero: módulo de liquidación de compras

Lógica de negocio de la tienda en línea **Mercado Sabanero**, ubicada en Sincelejo, Sucre. El proyecto implementa las funcionalidades relacionadas con el carrito de compras, IVA, descuentos, cupones, envío, liquidación del total y acumulación de puntos.

El desarrollo se realizó mediante **TDD (Test-Driven Development)**, siguiendo el ciclo **rojo, verde y refactor** en Python.

**Taller de Pruebas Ágiles: pruebas unitarias y TDD**  
Electiva Profesional en Ingeniería de Software — CECAR

**Equipo:** Ximena Barrera y Lizeth Mercado.

## Herramientas

| Necesidad | Herramienta |
|---|---|
| Lenguaje | Python 3.13 |
| Pruebas unitarias y parametrizadas | pytest |
| Dobles de prueba (inventario) | unittest.mock |
| Cobertura de código | pytest-cov |

## Funcionalidades

El sistema implementa las siguientes historias de usuario:

| Historia | Módulo | Responsable |
|---|---|---|
| HU-01 Agregar productos al carrito | `carrito.py` | Ximena |
| HU-02 Calcular el IVA | `iva.py` | Ximena |
| HU-03 Descuento por volumen | `descuentos.py` | Lizeth |
| HU-04 Usar cupones | `cupones.py` | Lizeth |
| HU-05 Calcular el envío y el total | `liquidacion.py` | Lizeth |
| HU-06 Acumular puntos | `puntos.py` | Ximena |
| Redondeo compartido (half-up) | `redondeo.py` | Ximena |

La liquidación integra los diferentes componentes del proceso de compra: carrito, descuentos, IVA, envío, total y puntos.

## Cómo ejecutar el proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/XimenaBarrera1/mercado-sabanero-tdd.git
cd mercado-sabanero-tdd
```

### 2. Crear el entorno virtual

```bash
py -m venv .venv
```

### 3. Activar el entorno virtual

En PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 5. Ejecutar las pruebas

```bash
pytest
```

El comando `pytest` ejecuta todas las pruebas y muestra el reporte de cobertura de líneas en la terminal. La configuración de cobertura se encuentra en `pytest.ini`.

## Resultado de las pruebas

El proyecto cuenta actualmente con:

- **58 pruebas automatizadas**
- **58 pruebas aprobadas**
- **100 % de cobertura de código**

Resultado de la última ejecución:

```text
58 passed in 0.55s

TOTAL    128    0    100%
```

La cobertura del 100 % corresponde a los módulos de la lógica de negocio incluidos en el proyecto.

## Estructura del proyecto

```text
mercado-sabanero-tdd/
│
├── src/
│   └── mercado_sabanero/
│       ├── __init__.py
│       ├── carrito.py
│       ├── cupones.py
│       ├── descuentos.py
│       ├── envio.py
│       ├── errores.py
│       ├── iva.py
│       ├── liquidacion.py
│       ├── puntos.py
│       ├── producto.py
│       └── redondeo.py
│
├── tests/
│   ├── test_carrito.py
│   ├── test_cupones.py
│   ├── test_descuentos.py
│   ├── test_envio.py
│   ├── test_iva.py
│   ├── test_liquidacion.py
│   ├── test_puntos.py
│   └── test_redondeo.py
│
├── docs/
│   └── defectos.md
│
├── requirements.txt
├── pytest.ini
└── README.md
```

## Flujo de trabajo con TDD

El desarrollo de cada funcionalidad siguió el ciclo:

1. **Rojo:** se escribe una prueba que inicialmente falla.
2. **Verde:** se implementa el código mínimo necesario para que la prueba pase.
3. **Refactor:** se mejora la implementación manteniendo todas las pruebas aprobadas.

Se utilizaron ramas independientes para cada historia de usuario, seguidas de Pull Requests hacia `main`.

Ejemplos de ramas:

```text
feat/hu-01-carrito
feat/hu-02-iva
feat/hu-03-descuento
feat/hu-04-cupones
feat/hu-05-envio-total
feat/hu-06-puntos
```

Los commits siguen una convención relacionada con el ciclo TDD:

```text
test:      pruebas
feat:      implementación
refactor:  mejora del código
```

Cada Pull Request fue revisado por la otra integrante del equipo.

## Reglas técnicas

- Los valores monetarios se manejan como **enteros en pesos colombianos, sin decimales**.
- El redondeo se realiza al peso más cercano utilizando la regla **half-up**; por ejemplo, `2.5` se redondea a `3`.
- Se utiliza una función propia `redondear()` debido a que `round()` de Python utiliza redondeo al par en determinados casos.
- El inventario se considera un servicio externo y se reemplaza mediante **mock** durante las pruebas.
- Las pruebas incluyen casos normales, límites y errores de las reglas de negocio.
- La cobertura se verifica mediante `pytest-cov`.

## Documentación de defectos

Los defectos identificados durante el desarrollo y las decisiones tomadas para corregirlos se registran en:

```text
docs/defectos.md
```

Este registro permite documentar los problemas encontrados durante el ciclo de desarrollo y su correspondiente solución.