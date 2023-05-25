'''
TITLE
    atgc_percentage.py

VERSION 
    1.2

AUTHOR
    Valentina Janet Arias Ojeda

DESCRIPTION
    Dada una secuencia de DNA, el programa identificará el número de ocurrencias de As, Gs, Ts, y Cs para posteriormente sacar el porcentage de AT y GC en la secuencia.

CATEGORY
    Nucleotide percentage


'''
# Se define función encargada de realicar el cálculo de porcentaje
def calcular_porcentajes(secuencia_dna):

    # Definimos un diccionario que almacenará el conteo de cada nucleótido
    conteo_nucleotidos = {'A': 0, 'T': 0, 'G': 0, 'C': 0}

    # Conteo de nucleótidos por caracter en la cadena en un ciclo for que recorra y vaya aumentando la cuenta en el diccionario
    for nucleotido in secuencia_dna:
        if nucleotido in conteo_nucleotidos:
            conteo_nucleotidos[nucleotido] += 1

    # Cálculo de porcentaje utilizando datos del diccionario
    total = sum(conteo_nucleotidos.values())
    at = ((conteo_nucleotidos['A'] + conteo_nucleotidos['T']) / total) * 100
    gc = ((conteo_nucleotidos['G'] + conteo_nucleotidos['C']) / total) * 100


    # Regresar porcentaje
    return at, gc

#######  Main #########

# Se introduce el código en un bloque try para hacer validaciones y manejo de excepciones en las partes del código que puedan ser problemáticas
try:
    # Se le pide al usuario que ingrese la ruta donde se encuentre el archivo con la secuencia de ADN
    path = input('Ingrese la ruta al archivo: ')

    # Abrir el archivo
    dna = open(path).read().rstrip('\n')

    # Validar si el archivo contiene solo caracteres válidos de ADN
    if set(dna) - set('ATGC'):
        raise ValueError("El archivo contiene caracteres no válidos de ADN.")

    # Llamar a la función para calcular los porcentajes y almacenarlos en dos variables nuevas
    porcentaje_at, porcentaje_gc = calcular_porcentajes(dna)

    # Impresión de resultados
    print("El porcentaje de AT es:", porcentaje_at)
    print("El porcentaje de GC es:", porcentaje_gc)

# Excepción en el caso de que el archivo no sea encontrado
except FileNotFoundError:
    print("Archivo no encontrado. Verifique la ruta e intente nuevamente.")
