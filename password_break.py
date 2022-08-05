for i in range(3):
    password = str(input("Enter the password..."))

    if password == "secret":
        print("Access granted...")
        break
else:
    print("3 incorrect pw attempts...youre locked out!")
