'''
TITLE
    atgc_percentage.py

VERSION 
    1.0

AUTHOR
    Valentina Janet Arias Ojeda

DESCRIPTION
    Dada una secuencia de DNA, el programa identificará el número de ocurrencias de As, Gs, Ts, y Cs para posteriormente sacar el porcentage de AT y GC en la secuencia.

CATEGORY
    Nucleotide percentage

ARGUMENTS
    None

'''
# Se le pide al usuario que ingrese la ruta donde se encuentre el archivo con la secuencia de dna
# Recibir del teclado la ruta al archivo
#file_name = input('Ingrese el nombre del archivo con la secuencia de DNA: ')
path = input('Ingrese la ruta al archivo: ')

# Abrir el archivo
dna = open(path).read().rstrip('\n')

# Conteo de nucleotidos por caracter en la cadena
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

# Todo archivo se debe cerrar
dna.close()