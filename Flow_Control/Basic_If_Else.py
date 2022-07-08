# Flow chart -> decision making process
# Flow control statements
# Boolean values, Boolean Operators and comparison operators
# elif = else if statement
# Falsy truthy strings values - blank string is falsy value -> for ints the value 0 or 0.0 is falsy, all others are truthy


# password = input("Enter the password: ")
# if password == 'swordfish':
#     print("\nAcces granted")
# else:
#     print("\nWrong Password!")

print("Enter your name: ")
name = input()
if name: # Or bettr this code: if name != '': --> Specifying if name is not equal to empty string the skip and print last line
    print("\nHi " + name + "," + "thanks for complying weak human!")
else:
    print(" The AI fears you...argh!")
