# Taller Mecánico

Repositorio para la asignatura de Programación Orientada a Objetos Seguro.

**Profesor:** Michael Arjel
**Institución:** Inacap

---

## Bitácora de Avances

### 25 de Agosto de 2026
- **Configuración Inicial:** Vinculación del directorio local con el repositorio de GitHub usando el CLI de GitHub (`gh auth`).
- **Limpieza:** Se eliminó la versión antigua del archivo `vehiculo.py` para construir el proyecto desde cero.
- **Clase Vehiculo (`vehiculo.py`):**
  - Se creó la clase principal del proyecto.
  - Se definieron los atributos privados `__patente`, `__anio` y `__en_taller` en el constructor, aplicando encapsulamiento y *type hints*.
  - Se crearon los métodos `ingresar()` y `entregar()` con validación de estado.
  - Se creó el método `tarifa_hora()` que retorna un valor fijo de 5000.
- **Script de Pruebas (`main.py`):**
  - Se creó el archivo de ejecución principal.
  - Se importó la clase `Vehiculo` y se instanciaron 3 objetos con datos ficticios.
  - Se probó la invocación de métodos y la impresión de la tarifa por hora en consola.
- **Documentación:** Se comentaron todas las líneas de código en ambos archivos (`vehiculo.py` y `main.py`) explicando paso a paso su funcionamiento con fines educativos.

### 7 de Septiembre de 2026
- **Clase Camion (`camion.py`):**
  - Se implementó su propio constructor `__init__()` que recibe `patente`, `anio` y `capacidad_carga` (número entero en kilos).
  - Invocación al constructor de la clase padre mediante `super().__init__(patente, anio)`.
  - Se definió el atributo propio `__capacidad_carga` como privado aplicando encapsulamiento.
  - Sobrescritura del método `tarifa_hora()` retornando un valor fijo de `40000`.
- **Sobrescritura de Tarifas por Tipo de Vehículo (`auto.py`, `moto.py`, `camion.py`):**
  - En `auto.py` (`Auto`): se reemplazó el `pass` e implementó `tarifa_hora()` retornando `25000`.
  - En `moto.py` (`Moto`): se reemplazó el `pass` e implementó `tarifa_hora()` retornando `15000`.
  - En `camion.py` (`Camion`): se implementó `tarifa_hora()` retornando `40000`.
- **Clase Base Abstracta y Métodos Abstractos (`vehiculo.py`):**
  - Se convirtió la clase `Vehiculo` en abstracta heredando de `ABC` (`from abc import ABC, abstractmethod`).
  - Se definió `tarifa_hora()` como método abstracto utilizando el decorador `@abstractmethod` con cuerpo en `pass` (sin retorno), obligando a las subclases a proporcionar su propia implementación.
- **Propiedades y Validaciones en Clase Base (`vehiculo.py`):**
  - **Propiedad `patente`:**
    - Se creó el getter `@property` para acceder al atributo privado `__patente`.
    - Se implementó el setter `@patente.setter` con validación estricta (mínimo 6 caracteres y sin espacios); lanza un `ValueError` si no se cumplen las condiciones.
    - Se actualizó el constructor `__init__()` para usar `self.patente = patente`, asegurando que la validación se ejecute automáticamente al instanciar cualquier vehículo o subclase.
  - **Propiedad de solo lectura `en_taller`:**
    - Se creó el getter `@property` para consultar el atributo privado `__en_taller`.
    - No se implementó setter, protegiendo el atributo de modificaciones externas arbitrarias.
    - Los métodos `ingresar()` y `entregar()` continúan gestionando directamente el estado interno.
- **Manejo Seguro de Excepciones con Try/Except (`main.py`):**
  - Se incorporó un bloque `try / except ValueError` en el script cliente para gestionar de forma segura los intentos de instanciación con datos no válidos (por ejemplo, una patente con espacios o menor a 6 caracteres).
  - **Justificación de diseño:** Siguiendo el principio de POO Seguro y separación de responsabilidades, la clase `Vehiculo` es responsable de hacer cumplir las reglas de negocio lanzando excepciones (`raise ValueError`) ante datos inválidos, mientras que la capa de ejecución (`main.py`) es la encargada de capturar (`except`) y manejar el error de manera controlada para el usuario, impidiendo la interrupción abrupta del sistema.
- **Documentación y Pruebas:**
  - Se documentaron y comentaron línea por línea todos los cambios en `auto.py`, `moto.py`, `camion.py`, `vehiculo.py` y `main.py`.
  - Se verificó la correcta ejecución de las validaciones, la captura controlada de excepciones con `try/except`, la restricción de instanciación de clases abstractas y la salida por consola del script principal.

