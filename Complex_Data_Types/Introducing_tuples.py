# The Tuple - similar to Lists
# Tuples are an ordered collection of elements in which the order of elements matters
# Tuples are initalised with () rather than [] which are for lists
# Tuples are classes

my_tuple = ()
print(type(my_tuple))

str_tuple = ("Hi", "Dave!")
int_tuple = (1, 2, 3, 4)
print("\n", int_tuple, str_tuple)
new_combined_tuple = int_tuple + str_tuple
print("\nCombined Tuple: ", new_combined_tuple)

print("\nPrinting new combined tuple 3 times: ", new_combined_tuple * 3)

# In Python, when you assign a value to a var seperated by commas, Python automatically interprets this as a Tuple
auto_assigned_tuple = 1, "Hi Family!", 51.5
print("\nPy auto assigns this , seperated values as a Tuple: ", auto_assigned_tuple)

# Fields are used to reference to elements in a tuple
a, b, c = auto_assigned_tuple
print("\nAssigning fields to variables:", a, b, c)

# Nested Tuples
nested_tuple = (1, 2, 3, (4, 5, 6))
print("\nNested tuple:", nested_tuple)

mixed_tuple = ("Mercedes", [13, 11, 9, 5], (66, 55, 44))
print("\nMixed tuple example: ", mixed_tuple)

another_tuple = ("D", "a", "v", "i", "d")
print("\nAnother_tuple at position [0]:", another_tuple[0])

# Accessing field in a mixed tuple
print("\nAccessing certain field in the mixed tuple:", mixed_tuple[1][1])

# Performing slicing ops on a Tuple
# Start at 0, goto end, slice in default steps of 1
sliced_tuple = another_tuple[0::]
print("\nSliced tuple result:", sliced_tuple)

# Index function
print("\nIndex function example, where is D:", sliced_tuple.index("D"))

# In function
print("\nIs the letter M in my tuple?", "M" in sliced_tuple)

# not in function
print("\nIs the letter M not in my tuple?", "M" not in sliced_tuple)

# Sum function
print("\nSum function example: ", sum(int_tuple))

# Conver tuple to a list
print("\nint_tuple converted to a list", list(int_tuple))

# Convert tuple to a set
new_int_tuple = (1, 1, 2, 2, 3, 3)
# Sets dont allow repeated or double values
print("\nnew_int_tuple converted to a Set", set(new_int_tuple))
