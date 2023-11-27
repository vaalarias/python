'''
    NAME
        genomic_analysis

    VERSION
        1.0

    AUTHOR
        Valentina Janet Arias Ojeda

    DESCRIPTION
        Crea una clase base GenomicSequence y tres clases derivadas: DNASequence, RNASequence y ProteinSequence. Cada una tiene su método analyze que muestra un mensaje indicando qué tipo de secuencia se está analizando.

    CATEGORY
       Analysis    

    USAGE
        python genomic_analysis.py <sequence> <type>

    ARGUMENTS
        <type> : DNA , RNA
'''

import sys

class GenomicSequence:
    def __init__(self, sequence):
        self.sequence = sequence

    def analyze(self):
        pass  # Este método será implementado en las clases hijas

class DNASequence(GenomicSequence):
    def analyze(self):
        print(f"Analyzing DNA sequence: {self.sequence}")
        # Lógica específica para análisis de ADN
    def transcribe_to_rna(self):
        # Reemplazar 'T' por 'U' para transcribir a ARN
        return self.sequence.replace('T', 'U')
    def count_at_gc(self):
        a_count = self.sequence.upper().count('A')
        t_count = self.sequence.upper().count('T')
        g_count = self.sequence.upper().count('G')
        c_count = self.sequence.upper().count('C')
        total_nucleotides = len(self.sequence)
        a_percentage = (a_count / total_nucleotides) * 100
        t_percentage = (t_count / total_nucleotides) * 100
        g_percentage = (g_count / total_nucleotides) * 100
        c_percentage = (c_count / total_nucleotides) * 100
        return a_percentage, t_percentage, g_percentage, c_percentage

class RNASequence(GenomicSequence):
    def analyze(self):
        print(f"Analyzing RNA sequence: {self.sequence}")
        # Lógica específica para análisis de ARN

    def translate(self):
        codon_table = {
            "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
            "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
            "UAU": "Y", "UAC": "Y", "UAA": "*", "UAG": "*",
            "UGU": "C", "UGC": "C", "UGA": "*", "UGG": "W",
            "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
            "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
            "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
            "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
            "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
            "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
            "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
            "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
            "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
            "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
            "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
            "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"
        }

        sequence = self.sequence.upper()
        protein_seq = ""
        for i in range(0, len(sequence), 3):
            codon = sequence[i:i+3]
            if len(codon) == 3:
                protein_seq += codon_table.get(codon, "X")
        return protein_seq
    def count_at_gc(self):
        a_count = self.sequence.upper().count('A')
        u_count = self.sequence.upper().count('U')
        g_count = self.sequence.upper().count('G')
        c_count = self.sequence.upper().count('C')
        total_nucleotides = len(self.sequence)
        au_percentage = ((a_count + u_count) / total_nucleotides) * 100
        gc_percentage = ((g_count + c_count) / total_nucleotides) * 100
        return au_percentage, gc_percentage

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python genomic_analysis.py <sequence> <type>")
        sys.exit(1)

    sequence = sys.argv[1].upper()
    sequence_type = sys.argv[2].upper()

    if sequence_type == 'DNA':
        dna_seq = DNASequence(sequence)
        dna_seq.analyze()
        transcribed_rna = dna_seq.transcribe_to_rna()  # Transcribir la secuencia de ADN a ARN
        print(f"\nTranscribed RNA sequence from DNA:\n{transcribed_rna}")
        at_gc_percentages = dna_seq.count_at_gc()  # Calcular porcentaje A, T, G, C en la secuencia de ADN
        print(f"\nPercentage of A in DNA sequence: {at_gc_percentages[0]:.2f}%")
        print(f"Percentage of T in DNA sequence: {at_gc_percentages[1]:.2f}%")
        print(f"Percentage of G in DNA sequence: {at_gc_percentages[2]:.2f}%")
        print(f"Percentage of C in DNA sequence: {at_gc_percentages[3]:.2f}%")
    elif sequence_type == 'RNA':
        rna_seq = RNASequence(sequence)
        rna_seq.analyze()
        translated_sequence = rna_seq.translate()
        au_gc_percentages = rna_seq.count_at_gc()
        print(f"\nTranslated protein sequence:\n{translated_sequence}")
        print(f"\nPercentage of AU in RNA sequence: {au_gc_percentages[0]:.2f}%")
        print(f"Percentage of GC in RNA sequence: {au_gc_percentages[1]:.2f}%")
    else:
        print("Invalid sequence type. Choose DNA or RNA.")
        sys.exit(1)
