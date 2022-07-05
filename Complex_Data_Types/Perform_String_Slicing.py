my_string = "The weather is cloudy today and everyday this week."
print(len(my_string))
print("\n", my_string[0:21])

# No start or end index means the whole string is included/shown etc
print(my_string[::2])
# Start at the end , (the len -1) goto the beginning ( 0 ) in steps of 1 ( Going backwards)
print(my_string[-1:0:-1])

# A string in Python is a class. So you can invoke functions on classes. Ive invoked the .split function on my_string which creates a new list of in this case words, divided up by spaces that was specified in the .split() function.
new_string = my_string.split()
print(new_string)
