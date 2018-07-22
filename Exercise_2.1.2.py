# An Introduction to Solving Biological Problems with Python: Exercise 2.1.2


# DNA and codon sequences given.
seq = "ATGGCGGTCGAATAGTTACTGACCTGA"
print(seq)
codon = "TAG"
codon_2 = "TAA"
codon_3 = "TGA"

# Determine if codons of interest are present in the sequence using conditional statements. Identify their position.
if (codon in seq) or (codon_2 in seq) or (codon_3 in seq):
    print('A stop codon has been found in the above DNA sequence.')
    print("The index position of the codons", codon + ",", codon_2, "and", codon_3, "is:", seq.find(codon), seq.find(codon_2), "and", seq.find(codon_3), "respectively.")
else:
    print('The DNA sequence does not contain any of the following codons:', codon + ",", codon_2 + ",", codon_3 + ".") 

    
    
