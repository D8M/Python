# The range type allows for generating a sequence of Intergers
a_range = range(10)
print("Range: ", a_range)
print("Range list: ", list(a_range))

for i in range(5):
    print(i, end=" ")
print()

a_range = range(10, 20)
print("Range: ", a_range)
print("Range list: ", list(a_range))

# starts at 10, goes to -1 but does not include it, goes down in steps of -1
a_range = range(10, -1, -1)
print("Range: ", a_range)
print("Range list: ", list(a_range))
