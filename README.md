# Cálculos de física con Python

Proyecto académico del curso Programación Básica con Python. Incluye tres programas para realizar cálculos físicos, guardar sus resultados en archivos TXT, consultar la información y eliminar registros.

## Programas incluidos

- **01_guardar_calculos.py:** solicita los datos, realiza cinco cálculos y guarda los datos y resultados en un archivo TXT.
- **02_leer_calculos.py:** abre el archivo indicado y muestra sus líneas numeradas.
- **03_eliminar_calculo.py:** elimina la línea seleccionada y actualiza el mismo archivo.

## Cálculos disponibles

| Cálculo | Fórmula |
|---|---|
| Periodo | T = 1 / f |
| Velocidad angular | w = (2 × 3.14) × f |
| Fuerza resultante | FR = m × a |
| Energía cinética | EC = 0.5 × m × v² |
| Energía potencial | EP = m × 9.8 × h |

Se utilizan los valores 3.14 para pi y 9.8 m/s² para la gravedad, según las indicaciones del ejercicio.

## Requisitos

- Python 3.6 o posterior.
- PyCharm u otro editor compatible con Python.
- No requiere instalar bibliotecas externas.

## Cómo ejecutar el proyecto

1. Descarga los archivos y coloca los tres programas `.py` en una misma carpeta.
2. Abre esa carpeta en PyCharm y configura un intérprete de Python.
3. Ejecuta `01_guardar_calculos.py`.
4. Escribe un nombre para el archivo, por ejemplo `calculos`, e introduce los valores solicitados.
5. Ejecuta `02_leer_calculos.py` y escribe el mismo nombre para consultar los resultados.
6. Ejecuta `03_eliminar_calculo.py`, escribe el nombre del archivo y selecciona la línea que deseas eliminar.
7. Vuelve a ejecutar el programa de lectura para comprobar el cambio.

Los archivos TXT se guardan junto a los programas. Si se ejecuta el primer programa con un nombre de archivo existente, su contenido se sobrescribe.

## Ejemplo de resultados

| Cálculo | Datos de entrada | Resultado esperado |
|---|---|---|
| Periodo | f = 2 Hz | 0.5 s |
| Velocidad angular | f = 5 Hz | Aproximadamente 31.4 rad/s |
| Fuerza resultante | m = 3 kg; a = 4 m/s² | 12 N |
| Energía cinética | m = 2 kg; v = 3 m/s | 9 J |
| Energía potencial | m = 10 kg; h = 10 m | 980 J |

Por la representación de decimales en Python, algunos resultados pueden mostrar cifras adicionales, como `31.400000000000002`.

## Validaciones y pruebas

El programa verifica entradas numéricas, evita la división entre cero y comprueba que la línea seleccionada exista. También informa cuando un archivo no existe o está vacío.

Se comprobó en PyCharm la creación del TXT, la lectura de los cinco cálculos y la eliminación de una línea con su posterior guardado.

## Conceptos practicados

Variables, operaciones matemáticas, funciones, condicionales, ciclos, listas, manejo de excepciones y lectura y escritura de archivos de texto.

## Desarrollo

Proyecto probado en PyCharm.
