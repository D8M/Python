# Check if an inputted num is divisible by 5 or 7 or both

num1 = int(input("\nEnter a number: "))

if num1 % 5 == 0 and num1 % 7 == 0:
    print("\nThis number is divisible by both 5 and 7 ")
elif num1 % 5 == 0:
    print("\nThis number is divisible by 5 ")
elif num1 % 7 == 0:
    print("This number is divisible by 7 ")
else:
    print("\nThis number is neither divisible by 5 or 7 ")
