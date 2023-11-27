
'''
TITLE
    genbank.py

VERSION
    1.0

AUTHOR
    Valentina Janet Arias Ojeda

DESCRIPTION
    Dada un archivo de GenBank, se busca el gen indicado y se parsea para obtener los datos como la secuencia, el transcrito y proteína asociada.

CATEGORY
    Sequence

ARGUMENTS
    FILE 
    GENES [GENES ...]

'''
import argparse
from Bio import SeqIO

def get_gene_info(file_path, genes):
    # Parsear el archivo GenBank
    for record in SeqIO.parse(file_path, "genbank"):
        for feature in record.features:
            # Verificar si el feature es un gen y si coincide con el nombre proporcionado
            if feature.type == "gene" and feature.qualifiers.get('gene') in genes:
                print(f"Gene: {feature.qualifiers['gene'][0]}")
                if 'translation' in feature.qualifiers:
                    print(f"Protein: {feature.qualifiers['translation'][0]}")
                if 'transl_table' in feature.qualifiers:
                    print(f"Transl Table: {feature.qualifiers['transl_table'][0]}")
                if 'translation' not in feature.qualifiers and 'pseudo' not in feature.qualifiers:
                    print("No protein information available")
                print("------")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Parse GenBank file for gene information')
    parser.add_argument('-f', '--file', type=str, help='Path to the GenBank file')
    parser.add_argument('-g', '--genes', nargs='+', help='Name(s) of the gene(s) to print info')
    args = parser.parse_args()

    if not args.file or not args.genes:
        parser.print_help()
    else:
        get_gene_info(args.file, args.genes)
