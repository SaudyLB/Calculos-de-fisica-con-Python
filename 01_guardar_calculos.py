# Proyecto 1 - Programación Básica con Python.
# Programa 1: realizar cinco cálculos y guardarlos en un archivo TXT.
import os
import math


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


def pedir_numero(mensaje, minimo=None, positivo=False):
    # Repetimos la pregunta cuando el dato no se puede utilizar.
    while True:
        try:
            numero = float(input(mensaje))
            if not math.isfinite(numero):
                print("Ingrese un número finito.")
            elif positivo and numero <= 0:
                print("El número debe ser mayor que cero.")
            elif minimo is not None and numero < minimo:
                print("El número debe ser mayor o igual que", minimo)
            else:
                return numero
        except ValueError:
            print("Ingrese un número; use punto para los decimales.")


def main():
    print("CÁLCULOS DE FÍSICA")
    nombre = pedir_nombre()
    carpeta = os.path.dirname(os.path.abspath(__file__))
    ruta = os.path.join(carpeta, nombre)

    # 1. Periodo: T = 1 / f. La frecuencia debe ser positiva.
    frecuencia_periodo = pedir_numero("Frecuencia para el periodo (Hz): ", positivo=True)
    periodo = 1 / frecuencia_periodo

    # 2. Velocidad angular: usamos exactamente 3.14, como pide el PDF.
    frecuencia_angular = pedir_numero("Frecuencia para la velocidad angular (Hz): ", minimo=0)
    velocidad_angular = (2 * 3.14) * frecuencia_angular

    # 3. Fuerza resultante: FR = m * a.
    # La aceleración puede ser negativa, según la dirección elegida.
    masa_fuerza = pedir_numero("Masa para la fuerza (kg): ", minimo=0)
    aceleracion = pedir_numero("Aceleración (m/s²): ")
    fuerza = masa_fuerza * aceleracion

    # 4. Energía cinética: EC = (0.5 * m) * v².
    # En Python, ** 2 eleva al cuadrado; ^ no sirve para esta operación.
    masa_cinetica = pedir_numero("Masa para la energía cinética (kg): ", minimo=0)
    velocidad = pedir_numero("Velocidad (m/s): ")
    try:
        energia_cinetica = (0.5 * masa_cinetica) * velocidad ** 2
    except OverflowError:
        print("Los valores son demasiado grandes. Ejecute de nuevo con otros datos.")
        return

    # 5. Energía potencial: EP = m * g * h, con gravedad fija de 9.8.
    # La altura puede ser negativa respecto al nivel de referencia.
    masa_potencial = pedir_numero("Masa para la energía potencial (kg): ", minimo=0)
    altura = pedir_numero("Altura respecto al nivel de referencia (m): ")
    gravedad = 9.8
    energia_potencial = masa_potencial * gravedad * altura

    # Evitamos guardar resultados infinitos por datos excesivamente grandes.
    resultados = [periodo, velocidad_angular, fuerza, energia_cinetica, energia_potencial]
    if not all(math.isfinite(resultado) for resultado in resultados):
        print("Los valores son demasiado grandes. No se guardó el archivo.")
        return

    # Cada cadena contiene los datos y el resultado de un cálculo.
    # No redondeamos los resultados antes de escribirlos.
    lineas = [
        f"Periodo: f={frecuencia_periodo} Hz; T={periodo} s\n",
        f"Velocidad angular: f={frecuencia_angular} Hz; pi=3.14; w={velocidad_angular} rad/s\n",
        f"Fuerza resultante: m={masa_fuerza} kg; a={aceleracion} m/s²; FR={fuerza} N\n",
        f"Energía cinética: m={masa_cinetica} kg; v={velocidad} m/s; EC={energia_cinetica} J\n",
        f"Energía potencial: m={masa_potencial} kg; g={gravedad} m/s²; h={altura} m; EP={energia_potencial} J\n"
    ]

    try:
        # 'w' crea el TXT o sobrescribe su contenido si ya existe.
        # 'with' cierra el archivo al terminar; UTF-8 conserva las tildes.
        with open(ruta, "w", encoding="utf-8") as archivo:
            archivo.writelines(lineas)
        print("Se guardaron los cinco cálculos en:", ruta)
    except OSError as error:
        print("No se pudo guardar el archivo:", error)


# Este bloque inicia el programa al ejecutarlo directamente.
if __name__ == "__main__":
    main()
