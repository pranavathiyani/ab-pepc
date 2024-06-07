# -*- coding: utf-8 -*-
"""amino_acid_composition.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1YebtHJU3a9oNapMztiEku0M2VToI_1Lm
"""

# amino_acid_composition.py

def amino_acid_composition(sequence):
    amino_acids = 'ACDEFGHIKLMNPQRSTVWY'
    composition = {aa: 0 for aa in amino_acids}
    total = len(sequence)

    for aa in sequence:
        if aa in composition:
            composition[aa] += 1

    for aa in composition:
        composition[aa] = (composition[aa] / total) * 100

    return composition

def process_dataset(dataset):
    compositions = []
    for sequence in dataset:
        compositions.append(amino_acid_composition(sequence))
    return compositions

def main(active_peptides, inactive_peptides):
    active_compositions = process_dataset(active_peptides)
    inactive_compositions = process_dataset(inactive_peptides)
    return active_compositions, inactive_compositions

if __name__ == "__main__":
    # Example usage
    active_peptides = ["ACDEFGHIKLMNPQRSTVWY", "ACDEFGHIKLMN"]
    inactive_peptides = ["QRSTVWYACDEFGHIKLMN", "HIKLMNPQRST"]

    active_compositions, inactive_compositions = main(active_peptides, inactive_peptides)
    print("Active Peptide Compositions:", active_compositions)
    print("Inactive Peptide Compositions:", inactive_compositions)