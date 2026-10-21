# Proyecto 1 - Programación Básica con Python, UNED.
# Programa independiente: eliminar una línea y guardar el mismo TXT.
import os


def pedir_nombre():
    # Solo pedimos un nombre: la carpeta siempre será la del programa.
    while True:
        nombre = input("Nombre del archivo TXT (ejemplo: calculos): ").strip()
        if nombre.lower().endswith(".txt"):
            nombre = nombre[:-4]
        if (not nombre or nombre in (".", "..")
                or any(caracter in nombre for caracter in '<>:"/\\|?*')
                or any(ord(caracter) < 32 for caracter in nombre)
                or nombre.endswith((" ", "."))):
            print("Escriba un nombre válido, sin carpetas ni caracteres especiales.")
        else:
            return nombre + ".txt"


def main():
    print("ELIMINACIÓN DE UN CÁLCULO")
    nombre = pedir_nombre()
    carpeta = os.path.dirname(os.path.abspath(__file__))
    ruta = os.path.join(carpeta, nombre)
    try:
        # Primero leemos todas las líneas y cerramos el archivo.
        with open(ruta, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
        if not lineas:
            print("El archivo está vacío. No hay cálculos para eliminar.")
            return

        for numero, linea in enumerate(lineas, start=1):
            print(f"{numero}. {linea.rstrip()}")

        # Solo aceptamos un entero que corresponda a una línea existente.
        while True:
            try:
                numero = int(input("Número de línea que desea eliminar: "))
                if 1 <= numero <= len(lineas):
                    break
                print("Seleccione una línea entre 1 y", len(lineas))
            except ValueError:
                print("Ingrese un número entero.")

        # Las listas empiezan en 0: la línea 1 está en la posición 0.
        del lineas[numero - 1]

        # Reescribimos el MISMO archivo con las líneas restantes.
        with open(ruta, "w", encoding="utf-8") as archivo:
            archivo.writelines(lineas)
        print("Línea eliminada. Archivo actualizado:", ruta)
    except FileNotFoundError:
        print("El archivo no existe. Revise el nombre y la carpeta.")
    except UnicodeError:
        print("El archivo debe ser un TXT con codificación UTF-8.")
    except OSError as error:
        print("No se pudo leer o actualizar el archivo:", error)


if __name__ == "__main__":
    main()
