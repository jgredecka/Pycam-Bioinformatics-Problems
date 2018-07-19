# An Introduction to Solving Biological Problems with Python: Exercise 1.4.2


# Print out the names of the amino acids that would be produced by the DNA sequence "GTT GCA CCA CAA CCG" according to the published DNA codon table. 
print("Valine", "Alanine", "Proline", "Glutamine", "Proline")

# Split this string into the individual codons and print the result.
DNA = "GTT GCA CCA CAA CCG"
codons = DNA.split()
print(codons)

# Use a dictionary to map between codon sequences and the amino acids they encode.
codonMap = {codons[0] : "Valine", codons[1] : "Alanine", codons[2] : "Proline", codons[3] : "Glutamine", codons[4] : "Proline"}

# Print each codon and its corresponding amino acid.
print(codons[0], "encodes", codonMap[codons[0]])
print(codons[1], "encodes", codonMap[codons[1]])
print(codons[2], "encodes", codonMap[codons[2]])
print(codons[3], "encodes", codonMap[codons[3]])
print(codons[4], "encodes", codonMap[codons[4]])

