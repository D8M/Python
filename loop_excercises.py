# Loop Eccers

# Print the cubes of all the elements in a list using a for loop

results = []
list_of_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in list_of_nums:
    results.append(i ** 3)

print(results)

#####################################################################

# Given a 2D list, create a 1D list

two_d_list = [['volkswagen', 'Mercedes', 'BMW'], ['Honda', 'Toyota', 'Mazada']]

one_d_list = []

for i in two_d_list:

    for j in i:
        one_d_list.append(i)

    print(one_d_list)

########################################################################

# Use Range to print out all leap years in 21 century
num_list = []
for i in range(2000, 2100, 4):
    num_list.append(i)
    print(num_list)
