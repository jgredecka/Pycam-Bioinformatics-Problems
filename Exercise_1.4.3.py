# An Introduction to Solving Biological Problems with Python: Exercise 1.4.3


# 1-letter code lysozyme protein sequence given.
lysozyme = "MKALIVLGLVLLSVTVQGKVFERCELARTLKRLGMDGYRGISLANWMCLAKWESGYNTRATNYNAGDRSTDYGIFQINSRYWCNDGKTPGAVNACHLSCSALLQDNIADAVACAKRVVRDPQGIRAWVAWRNRCQNRDVRQYVQGCGV"

# Identify the unique residues present in the sequence.
residues = list(lysozyme)
uniqueResidues = set(residues)

# Create a list of alphabetically sorted unique residues.
key = list(uniqueResidues)
key.sort()
print(key)

# Build a dictionary which contains a mapping of residues to their abundance in the protein sequence.
residueMap = {}
residueMap[key[0]] = lysozyme.count("A")
residueMap[key[1]] = lysozyme.count("C")
residueMap[key[2]] = lysozyme.count("D")
residueMap[key[3]] = lysozyme.count("E")
residueMap[key[4]] = lysozyme.count("F")
residueMap[key[5]] = lysozyme.count("G")
residueMap[key[6]] = lysozyme.count("H")
residueMap[key[7]] = lysozyme.count("I")
residueMap[key[8]] = lysozyme.count("K")
residueMap[key[9]] = lysozyme.count("L")
residueMap[key[10]] = lysozyme.count("M")
residueMap[key[11]] = lysozyme.count("N")
residueMap[key[12]] = lysozyme.count("P")
residueMap[key[13]] = lysozyme.count("Q")
residueMap[key[14]] = lysozyme.count("R")
residueMap[key[15]] = lysozyme.count("S")
residueMap[key[16]] = lysozyme.count("T")
residueMap[key[17]] = lysozyme.count("V")
residueMap[key[18]] = lysozyme.count("W")
residueMap[key[19]] = lysozyme.count("Y")

# Print the result to the screen.
print(residueMap)
