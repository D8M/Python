# name var been assigned to typed in text
name = input("First and last names to be reversed: ")
# Words var has a space included explicity .split thing
words = name.split(" ")
for word in words:  # Creates for loop to iterate over the Words
    # Looks for last letter or index and goes back -1
    lastindex = len(word) - 1
    # Uses index var to loop over the range starting at the last index and stepping down to zero
    for index in range(lastindex, -1, -1):
        # Printing each letter of the word buy its index or slice with no char just an empty string at the end of the print
        print(word[index], end='')
    # After first word is printed it prints a space ' ' and goes back for second word
    print(end='')
print(end='\n')  # When its done it prints a new line char at the end...


# name var been assigned to typed in text
name = input("First and last names to be reversed: ")
first, last = name.split()
# Negative slicing is used by using a full slice starting at the beginning going until the end, stepping by -1 each time
print(first[::-1], last[::-1])
