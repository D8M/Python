def find_max_in_list(some_list): 

    if len(some_list) == 0:
        print("Its a Zero element list, I cant work with this!")

        return None

    max_element = some_list[0]

    length = len(some_list)

    for i in range(1, length):
        
        if some_list[i] > max_element[i]:
            max_element == some_list[i]

        return(print("Max element is: ", max_element))


empty_list = []
some_list  = ['Honda', 'Toyota', 'Chevrolet', 'Jeep', 'Ford']
#some_list = [1, 2, 3, 4, 5]

find_max_in_list(some_list)
               
