'''
TITLE
    rna_sequence.py

VERSION
    1.1

AUTHOR
    Valentina Janet Arias Ojeda

DESCRIPTION
    Dada una secuencia de RNA, el programa identificará la posición en la que se encuentran los codones de inicio y de paro e imprimirá la secuencia entre ellos.

CATEGORY
    Secuence identification

ARGUMENTS
    None

'''
# Secuencia
dna = 'AAGGTACGTCGCGCGTTATTAGCCTAAT'

# Codon de inicio y paro
codon_ini = 'TAC'
codon_paro = 'ATT'

# sección problemática dentro de un bloque try para generar una excepción

try:
    # Busqueda del patron
    inicio = dna.index(codon_ini)
    fin = dna.index(codon_paro)
    
    # Cortar la secuencia
    intermedia = dna[inicio:fin]
    
    print('El fragmento que trascribe empieza en la posición', inicio, 'y termina en', fin)
    print(f'\nFragmento que será RNA (codón inicio: {codon_ini}, codón de paro: {codon_paro}) es:\n{intermedia}')

#  Si alguno de los codones no se encuentra en la secuencia de ADN, se genera una excepción ValueError.
except ValueError:
    raise ValueError('No se encontró el codón de inicio y/o el codón de paro en la secuencia de ADN.')
