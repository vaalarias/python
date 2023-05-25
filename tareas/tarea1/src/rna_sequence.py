'''
TITLE
    rna_sequence.py

VERSION
    1.0

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

# Busqueda del patron
inicio = dna.find(codon_ini)
fin = dna.find(codon_paro)

# Cortar la secuencia 
intermedia = dna[inicio:fin]
print('El fragmento que trasncribe empieza en la posicion ',inicio, ' y termina en ',fin)
print(f'\nFragmento que será RNA  (codón inicio: {codon_ini}, codón de paro ={codon_paro}) es: \n{intermedia}')

### Extra

# print('El codon AUG empieza en la posicion: ')  
# print(inicio)

# print('El codon AUG empieza en la posicion: '+ str(inicio)) 