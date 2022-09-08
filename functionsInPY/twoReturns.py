def add_sub(x,y):
    
    add_result = x + y
    sub_result = x - y

    return add_result, sub_result

print(add_sub(12,13)) # returns as a tuple


def positive_or_negative(num):

    if num > 0:
        return(print("Positive number"))
    
    elif num < 0:
        return(print("Negative number"))
    
    else:
        return(print("Zero"))
    


result_1, result_2 =  add_sub(177,86)
print(result_1)
print(result_2)

positive_or_negative(0)


