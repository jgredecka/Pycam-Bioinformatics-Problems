# Introduction to Solving Biological Problems with Python: # Exercise 1.3.2
# This program manipulates a simple string variable.


# 1. Create a string variable with your full name in it. Split the string into a list, and print out your surname.
fullName = "Justyna Gredecka"
splitName = fullName.split(" ")
surname = splitName[1]
print(surname)

# 2. Check if your surname contains the letter "e", and print out the position of this letter in the string.
checkLetter = "e" in surname
findLetter = surname.find("e")
print("The index position of the first 'e' in the surname Gredecka is", findLetter)
        


