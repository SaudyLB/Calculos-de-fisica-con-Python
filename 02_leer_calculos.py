# Proyecto 1 - Programación Básica con Python, UNED.
# Programa independiente: leer y mostrar el archivo TXT.
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
    print("LECTURA DE CÁLCULOS")
    nombre = pedir_nombre()
    # Buscamos el TXT en la misma carpeta que contiene este programa.
    carpeta = os.path.dirname(os.path.abspath(__file__))
    ruta = os.path.join(carpeta, nombre)
    try:
        # El modo 'r' permite leer sin modificar el contenido.
        with open(ruta, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
        if not lineas:
            print("El archivo está vacío.")
        else:
            # Numeramos desde 1 para identificar fácilmente cada cálculo.
            for numero, linea in enumerate(lineas, start=1):
                print(f"{numero}. {linea.rstrip()}")
    except FileNotFoundError:
        print("El archivo no existe. Revise el nombre y la carpeta.")
    except UnicodeError:
        print("El archivo debe ser un TXT con codificación UTF-8.")
    except OSError as error:
        print("No se pudo leer el archivo:", error)


if __name__ == "__main__":
    main()
