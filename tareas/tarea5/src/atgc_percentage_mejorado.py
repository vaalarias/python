'''
TITLE
    atgc_percentage.py

VERSION
    1.1

AUTHOR
    Valentina Janet Arias Ojeda

DESCRIPTION
    Dada una secuencia de DNA, el programa identificará el número de ocurrencias de As, Gs, Ts, y Cs para posteriormente sacar el porcentage de AT y GC en la secuencia.

CATEGORY
    Nucleotide percentage

ARGUMENTS
    None

'''
# Dado que se pueden generar problemas al recibir la ruta del archivo lo meteremos en un bloque try

try:
    # Recibir del teclado la ruta al archivo
    path = input('Ingrese la ruta al archivo: ')

    # Abrir el archivo con with para abrir el archivo de manera segura
    with open(path) as file:
        dna = file.read().rstrip('\n')
    
    # Conteo de nucleótidos por caracter en la cadena
    adeninas = dna.count('A')
    timinas = dna.count('T')
    guaninas = dna.count('G')
    citosinas = dna.count('C')

    # Conteo total
    total = adeninas + timinas + guaninas + citosinas
    at = ((adeninas + timinas) / total) * 100
    gc = ((guaninas + citosinas) / total) * 100

    # Impresión de resultados
    print("El porcentaje de AT es:", at)
    print("El porcentaje de GC es:", gc)

# Excepción en el caso de que no se pueda abrir el archivo por error en el input.

except FileNotFoundError:
    raise FileNotFoundError("No se encontró el archivo en la ruta especificada.")

# Si no se puede abrir el archivo

except IOError:
    raise IOError("Ocurrió un error al abrir el archivo.")
