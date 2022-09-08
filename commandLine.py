import sys

#Print Arguments
print("Number of arguments: ", len(sys.argv), ' arguments.')
print("Type of sys.argv: ", type(sys.argv))
print("Arguments ", sys.argv)

# Remove Arguments
sys.argv.remove(sys.argv[0])

print("Arguments ", sys.argv)

# Sum up the arguments
arguments = sys.argv
sum = 0
for arg in arguments:
    try:
        number = int(arg) # converting strings(args) to ints
        sum = sum + number
    except Exception:
        print("Sorry...Bad Input!")

print(sum)


