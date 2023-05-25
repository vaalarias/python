
'''
TITLE
    atgc_count.py

VERSION 
    1.0

AUTHOR
    Valentina Janet Arias Ojeda

DESCRIPTION
    Dada una secuencia de DNA, el programa identificará el número de ocurrencias de As, Gs, Ts, y Cs.

CATEGORY
    Nucleotide count

ARGUMENTS
    None

'''
# Se pide al usuario introducir una secuencia de DNA para almacenar como string.

dna = input("Introduce una secuencia de DNA: ")

# Se declaran 4 variables; cada una almacenará el número de ocurrencias en la cadena ingresada.

adeninas = dna.count('A')
guaninas = dna.count('G')
citosinas = dna.count('C')
timinas = dna.count('T')

# Se imprime el número de ocurrencias por variable y la secuencia.

print("La secuencia ingresada es:", dna)
print("El número de As es:", adeninas)
print("El número de Gs es:", guaninas)
print("El número de Cs es:", citosinas)
print("El número de Ts es:", timinas)