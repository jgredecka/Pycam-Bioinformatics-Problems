# Introduction to Solving Biological Problems with Python: Exercise 1.3.1
# This program manipulates and modifies a protein sequence consisting of four different amino acids.

# Create four codon/amino acid variables
serineS = "AGT"
leucineL = "CTT"
tyrosineY = "TAT"
cystineC = "TGT"

# Create a list of codons for the protein CLYSY and print its sequence.
codonList = [cystineC, leucineL, tyrosineY, serineS, tyrosineY]
print("The codon list for the protein sequence CLYSY is as follows:", codonList)

# Calculate and print the length of the sequence 
length = len(codonList)
print("This protein sequence consists of", length, "amino acids")

# Print the DNA sequence of the last codon
lastAminoAcid = codonList[-1]
print("The last codon of this sequence is", lastAminoAcid)

# Create two more variables for the DNA sequence of a start codon and a stop codon
startCodon = "AAT"
stopCodon = "TTA"

# Replace the first element of the codon list with the start codon and append the stop codon to the end of the list. Print the result.
codonList[0] = startCodon
codonList.append(stopCodon)
print("Start codon AAT and stop codon TTA have now been added to the sequence:", codonList)

