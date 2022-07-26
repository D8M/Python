# Divide a list

list_nums = [10, 11, 12, 13, 15, 23, 24, 27, 77, 66, 45, 89, 100, 1]
len_of_list = len(list_nums)

print("\nNumbers before slicing are: %s" % list_nums)
print("\nLength of Numbers before slicing are: %s" % len_of_list)

half = int(len_of_list/2)

list_num1 = list_nums[:half]
list_num2 = list_nums[half:]

print("\nFirst half: %s" % list_num1)
print("\nSecond half: %s" % list_num2)
