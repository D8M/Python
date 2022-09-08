value_int = int(input("Enter an integer: "))
length = 0

while value_int > 0:
    value_int //= 10
    length +=1
print("Number of digits: ", length)
