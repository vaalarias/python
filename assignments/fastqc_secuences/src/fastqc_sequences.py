'''
    NAME
        genomic_analysis

    VERSION
        1.0

    AUTHOR
        Valentina Janet Arias Ojeda

    DESCRIPTION
        El programa recibe la ruta a un archivo de texto plano con una secuencia de DNA en formato fastq y obtiene el número de secuencias con una calidad menor a una línea de corte establecida

    CATEGORY
       Analysis    

    USAGE
        python fastqc_sequences <sequence> <type>

    ARGUMENTS
        <File name/path>
        <Umbral> 
'''


import sys
from Bio import SeqIO

def filtro_calidad(archivo, umbral, debajo=True):
    count = 0
    with open(archivo, "r") as handle:
        for record in SeqIO.parse(handle, "fastq"):
            avg_quality = sum(record.letter_annotations["phred_quality"]) / len(record)
            if debajo and avg_quality < umbral:
                count += 1
            elif not debajo and avg_quality >= umbral:
                count += 1
    
    if debajo:
        print(f"Secuencias debajo del umbral: {count}")
    else:
        print(f"Secuencias arriba del umbral: {count}")

# Verificar si se proporciona el nombre del archivo como argumento
if len(sys.argv) < 4:
    print("Uso: python script.py archivo umbral debajo(opcional)")
else:
    archivo = sys.argv[1]
    umbral = int(sys.argv[2])
    debajo = True if len(sys.argv) < 5 else sys.argv[3].lower() == 'true'
    filtro_calidad(archivo=archivo, umbral=umbral, debajo=debajo)
