# An Introduction to Solving Biological Problems with Python.
# Exercises 2.2.1 and 2.2.2


# Create a 15-base sequence where each element is an individual base of DNA. Print the length of the sequence.
seq = ["A", "T", "C", "T", "G", "C", "C", "A", "G", "A", "T", "T", "C", "G", "A"]
print(seq)
print("The number of bases in the sequence is", len(seq))

print()

# Create a for loop to ouput every base of the sequence on a new line.
print("The individual bases are:")
for base in seq:
    print(base)
    
print()

# Create a while loop that starts at the third base in the sequence and outputs every third base until the 12th.
print("Every third base is:")
baseNo = 2
while baseNo <= 11:
    print(seq[baseNo])
    baseNo = baseNo + 3
