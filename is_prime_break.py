num = int(input("Enter a number: "))

for i in range(2, num//2):
    if num % i == 0:

        print("Its not a prime number")
        break

else:
    print(num, " is a prime number!")
    
