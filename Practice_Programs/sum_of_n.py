num = int(input("Enter your number: "))

temp1 = str(num)
temp2 = temp1 + temp1
temp3 = temp1 + temp2 + temp1

total = num + (int(temp2) + int(temp3))

print(temp1, '+', temp2, '+', temp3, '=', total)
