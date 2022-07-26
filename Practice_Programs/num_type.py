# Checks num to decide type

var = 1+2j

if(type(var) == int):
    print("\nType of variable is an integer")
elif(type(var) == float):
    print("\nType of variable is an float")
elif(type(var) == complex):
    print("\nType of variable is an complex")
else:
    print("\nType of variable is unknown!")
