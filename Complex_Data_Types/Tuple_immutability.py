# tuples and Strings are different. Tuples are immutable. Tuples, once created, cannot be changed or updated in any way.
# So, if you need an immutable collection use tuples rather than lists.
# tuple fields cannot be deleted individually, but whole Tuples can, use 'del' keyword

int_tuple = (1, 2, 3, 4)
# print("\nTrying to assign new value to field 0", int_tuple[0] = 4) Wont compile tuple immutability error

# The tuple itself is immutable , but any lists within it are not
mixed_tuple = ("Mercedes", [13, 11, 9, 5], (66, 55, 44))
# print("\nChanging List in a mixed tuple by assigning new value of 100: ", mixed_tuple[1][1] = 100) Doesnt wish to work either Tuple Immutability in action

# Tuple Zip function works with lists too ;)

tuple_a = (1, 2, 3, 4, 5, 6, 7)
tuble_b = ("a", "b", "c", "d", "e", "f", "g")

zipped = zip(tuple_a, tuble_b)
# Result is an Object. Each tuple will have 1 field from a, and 1 from b
print("\nZipped Tuple: ", zipped)
result = tuple(zipped)  # or result = list(zipped) results in a list of tuples
print("\nnew tuple of tuples : ", result)

# If you wish to extract the oringinal tuples from the zipped result call zip with an *
tuple_a, tuble_b = zip(*result)
print("\nUnzipped result: ", tuple_a, tuble_b)
