# Swappie Student list example

# list_students = ["Kate", "James", "Conor", "Emma", "Ben", "Charlie", "Lionel", "Lionel"]

# print("\n Student list: ", list_students)

# print("\nNumber of Students: ", len(list_students))

# student_set = set(list_students)
# print("\nNew Student list: ", list(student_set))
# print("\nLength of modified Student list: ", len(student_set))
# print("\nThere are %s duplicate elements" %(len(list_students) - len(student_set)))

#################################################################################

list_students = ["Kate", "James", "Conor",
                 "Emma", "Ben", "Charlie", "Lionel", "Lionel"]

len_list_students = len(list_students)

len_set_students = len(set(list_students))

if len_list_students == len_set_students:
    print("\nThere are no duplicate elements")

else:
    print("\nThere are {} duplicate elements".format(
        len_list_students - len_set_students))
