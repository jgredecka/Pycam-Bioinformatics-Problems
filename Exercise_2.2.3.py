# An Introduction to Solving Biological Problems with Python: Exercise 2.2.3

# A 15-base DNA sequence given.
seq = ["A", "T", "C", "T", "G", "C", "C", "A", "G", "A", "T", "T", "C", "G", "A"]

# Create a variable 'gc' which will be used to calcuate the GC content of the sequence.
gc = []

# Output every base in the sequence alongside its index on a new line.
for index, base in enumerate(seq):
    print(index, base)

# Calculate the percentage content of Guanine and Cytosine present in the DNA sequence. 
for base in seq:
    if base == "G" or base == "C":
        gc.append(base)   

gc_percentage = (len(gc)/len(seq))*100
print("The GC content of the above DNA sequence is", "{:.2f}%".format(gc_percentage))
 
