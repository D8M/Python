response = ""

while True:

    response = input("\nWhats the Capital of Egypt? ")

    if response == "quit":
        print("The correct answer is Cairo. Better Luck next time!")
        break

    if response.upper() == "CAIRO":
        print("That is the correct answer!")
        break

    else:
        print("Thats not correct, try again...")

        

    

