# Sistema de Turnos Hospitalarios

## Integrantes
  - Lenain, Juan Pablo
  - Rivas, Martin Gabriel
  - Lezcano Genes, Joshua David
  - Manassero, Alejandro
  - Ojeda, Ignacio

## Comisión
  Comisión 2

## Descripción general del sistema

Este proyecto es un sistema de turnos hospitalarios desarrollado en Python y ejecutado por consola. Su objetivo es administrar la atención de pacientes en un centro de salud, permitiendo registrar pacientes, solicitar turnos, asignarlos según especialidad médica, consultar turnos pendientes, atender pacientes según prioridad y visualizar estadísticas básicas.

El sistema valida los datos ingresados por el usuario y controla la disponibilidad de turnos para cada especialidad. Además, se encuentra organizado en diferentes módulos para separar las funcionalidades principales y facilitar la lectura, mantenimiento y comprensión del código.

A través de este proyecto se aplican contenidos trabajados durante la materia, como estructuras condicionales, ciclos, funciones, validaciones, acumuladores, contadores, modularización y manejo básico de errores.

## Instrucciones de ejecución

Para ejecutar el sistema, es necesario tener instalado Python en la computadora.

### Versión de Python requerida

Este proyecto requiere **Python 3.10 o superior**.

Se recomienda usar Python 3.10, 3.11, 3.12 o 3.13, ya que el código utiliza la estructura `match/case`, disponible a partir de Python 3.10.

Para verificar la versión instalada, abrir una terminal o consola y ejecutar:

```bash
python --version
```

o, en algunos sistemas:

```bash
python3 --version
```

### Descargar el proyecto

Clonar el repositorio desde GitHub o GitLab:

```bash
git clone URL_DEL_REPOSITORIO
```

Luego ingresar a la carpeta del proyecto:

```bash
cd sistema-turnos-hospitalarios
```

### Ejecutar el sistema

El archivo principal del sistema es `main.py`.

En Windows, ejecutar:

```bash
python main.py
```

En Mac o Linux, ejecutar:

```bash
python3 main.py
```

### Uso del sistema

Una vez ejecutado el programa, se mostrará un menú por consola con las opciones disponibles:

1. Registrar paciente.
2. Pedir un turno.
3. Ver turnos pendientes.
4. Atender siguiente turno.
5. Ver estadísticas.
6. Salir.

El usuario debe ingresar el número correspondiente a la opción que desea utilizar y seguir las instrucciones que aparecen en pantalla.

### Dependencias

El sistema no requiere instalar librerías externas.

El proyecto utiliza únicamente archivos propios del sistema, organizados en distintos módulos Python, como:

* `main.py`
* `altas.py`
* `solicitar_turno.py`
* `asignar_turno.py`
* `atender_turno.py`
* `ver_turnos.py`
* `estadisticas.py`
* `validaciones.py`

Por este motivo, no es necesario ejecutar `pip install` ni instalar paquetes adicionales.

### Aclaración importante

El sistema debe ejecutarse desde la carpeta donde se encuentra el archivo `main.py`, ya que desde allí se importan los demás módulos del proyecto.

Los datos cargados durante la ejecución, como pacientes y turnos, se mantienen en memoria mientras el programa está abierto. Al cerrar el sistema, la información se pierde, ya que esta versión no utiliza una base de datos ni archivos de persistencia.

## Uso de AI

Durante el desarrollo del proyecto se utilizó ChatGPT como herramienta de apoyo para orientar la organización del código, resolver dudas puntuales de programación, revisar errores y mejorar la modularización del sistema.

Las respuestas generadas por la IA no fueron incorporadas de manera automática, sino que fueron analizadas, adaptadas y probadas por el grupo antes de integrarlas al proyecto. En cada caso, se verificó que las soluciones propuestas fueran coherentes con la consigna, compatibles con el funcionamiento general del sistema y comprensibles para poder explicarlas y defenderlas técnicamente.

De esta manera, la IA fue utilizada como una herramienta de asistencia y aprendizaje, pero las decisiones finales sobre el código, la estructura del programa y su funcionamiento fueron tomadas por el grupo.
