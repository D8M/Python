# While loop
from ast import Continue
from unittest import result


# counter = 3
# while counter >= 0:
#     print("Counting Down: ", counter)
#     counter -= 1  # counter = counter -1

# while counter > 0:
#     print("Never executes suite")
#     print("When condition is false...")

# # while 1:
# #     print("executes at least once")
# #     if not counter:
# #       break

# names = ['Tom', 'Ellen']  # list
# while names:
#     print(names.pop(), "is going")

# results = [1, 0, 1]  # list
# processed = 0
# passed = 0

# while results:  # (are true) #list with elements above automatically considered true
#     processed += 1  # processed = processed +1
#     result = results.pop()  # popping off LAST value and storing it in result var
#     if not result:  # if not a true value, ie a zero or false vlaue, it doesnt go on to continue below
#         continue  # goes back to while start above
#     passed += 1
# else:
#     print("Processed: ", processed, "Passed", passed)

# # The For Loop
# for elem in range(10):
#     print(elem, end='')
# print()#positining print method here means for loop will print across the screen on a new line

# for elem in range(1, 6):  # start at 1 go up to 5 dont include 6
#     print(elem, end='')
# print()

# for elem in range(5, -1, -1):  # countdown from 5 to zero inclusive in steps of -1
#     print("Countdown: ", elem)

# for char in "String":
#     print(char, end='')
# print()

# for tup in (1,3,5,7):
#     print(tup)

# for val in ['hey', 'hi', 'hello']:
#     print(val)

# greek = {'Alpha': 1, 'Beta': 2, "Gamma": 3}
# for key in greek:
#     if key =='Beta':
#         continue
#     print(key, greek[key])

# for outer in range(2,10):
#     for inner in range(2, outer):
#         if not outer % inner:
#             print(outer,'=', inner, '*', int(outer / inner))
#             break
#         else:
#             print(outer, 'Is Prime')

#########################################################
# If Statements

age = 0
if age:
    print("False so no printing")

age = 1
if age:
    print("True so printing")
