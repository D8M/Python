# Find common chars in input

string1 = input("\nEnter first string: ")

string2 = input("\nEnter second string: ")

set_1 = set(string1)
set_2 = set(string2)

commmon_char = set_1.intersection(set_2)

print("\nCommon letters: ", list(commmon_char))
