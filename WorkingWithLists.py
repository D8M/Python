import PySimpleGUI as sg
# Working With Python Lists ->
# Methods ->
# Methods are functions called on values ->

# spam = ['hello', 'hi', 'howdy', 'heya']  # All lists have a method called index
# print(spam.index('hello'))  # Index Method is attached or called upon a certain value. This is the index location in the List variable called Spam, containing the String Hello. Spam contains the actual list

# spam = ['snark', 'piddles', 'flumpalump', 'digby', 'piddles']
# print(spam.index('piddles'))

# # Append and insert are List methods only
# # Appends list method adds new value to end of the list
# spam.append('Boogyboo')
# print(spam)  # No return values assigned to the variable, Dont do spam = spam.append(0 ,x) You just call the method itself

# # The 0 represents where in the list the value is to go
# spam.insert(0, '2Tails')
# print(spam)  # No return values

# spam = ['cat', 'rat', 'bat', 'sea mannity']
# spam.remove('bat')  # Specifiy that you remove an actual value from anywhere in the list rather than a certain index location, only the first time the value appears will be removed
# print(spam)

# spam = [2, 7, 9, 23, 91.75, 21, 6, 6, 55, 9.0, -1.1]
# spam.sort()  # ASCIIbetical ordering and Uppercase letters first
# print(spam)

# spam = ['snark', 'piddles', 'flumpalump', 'digby', 'piddles']
# spam.sort(reverse=True)
# print(spam)

# spam = ['a', 'b', 'c', 'd', 'A', 'B', 'C', 'D']
# spam.sort(key=str.lower)  # true alphabetical sorting
# print(spam)

layout = [ #list of lists 
[sg.Text("Text"), sg.Spin(["item 1", "Item 2"])], 
[sg.Button("Button")],
[sg.Input()],
[sg.Text("Test"), sg.Button("Test Button")]
]

sg.Window("Converter", layout).read() # Reads Input
