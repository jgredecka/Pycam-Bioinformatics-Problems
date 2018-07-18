# Introduction to Solving Biological Problems with Python: Exercise 1.4.1


# 1. Split the sequence into its component amino acid codes and print the result.
protein = "MPISEPTFFEIF"
aminoAcids = list(protein)
print(aminoAcids)

# 2. Use a set to establish the unique amino acids in the protein and print the result.
uniqueAminoAcids = set(aminoAcids)
print("The unique amino acids in the protein MPISEPTFFEIF are:", uniqueAminoAcids)
