# Basic Quiz Game

# capitalGuess = input("What is the capital if Ireland? ")
# numberOfGuesses = 1

# while capitalGuess != "Dublin":
#     numberOfGuesses = numberOfGuesses + 1
#     capitalGuess = input("Guess again. ")

# print("You guessed it! It took you " + str(numberOfGuesses) + " guesses")

####################################################################################

# initialSalesGoal = 20000
# multiplier = 100

# for monthlyGoal in range(1,13):
#     monthlySalesGoal = initialSalesGoal + (monthlyGoal * multiplier)
#     print("Your sales goal for the month " + str(monthlyGoal) + " is " + str(monthlySalesGoal)) #str(converting numberic values to strings here)
# print("Good luck with your sales.")

#####################################################################################

# Basic Quiz Game Updated with break

# capitalGuess = input("What is the capital if Ireland? ")
# numberOfGuesses = 1

# while capitalGuess != "Dublin":
#     numberOfGuesses = numberOfGuesses + 1
#     if numberOfGuesses > 3:
#         print("Game OVER!!!!")
#         break
#     capitalGuess = input("Guess again. ")
# if numberOfGuesses <= 3:
#     print("You guessed it! It took you " + str(numberOfGuesses) + " guesses")

#######################################################################################

# from operator import contains


# initialSalesGoal = 20000
# multiplier = 100

# for monthlyGoal in range(1,13):
#     if monthlyGoal == 6:
#         print("Holiday month, no goals for month 6.")
#         continue
#     monthlySalesGoal = initialSalesGoal + (monthlyGoal * multiplier)
#     print("Your sales goal for the month " + str(monthlyGoal) + " is " + str(monthlySalesGoal)) #str(converting numberic values to strings here)
# print("Good luck with your sales.")

##########################################################################################

# Pass in a else statement example

# annualMilesFlown = 202000
# newCustomer = True # Boolean var set to false here

# if annualMilesFlown >= 500000:
#     print("You are Gold level Customer")

# elif annualMilesFlown >= 400000:
#     print("You are Silver level Customer")

# elif annualMilesFlown >= 200000 and newCustomer: # Here, nweCustomer is refering to itself becomes True
#     pass

# elif annualMilesFlown >= 200000:
#     pass
# else:
#     print("Up and Coming Customer.")

# # NB: This line outide if statement --> not indented
# print("Thank you for flying with us.")

#################################################################################################

# Nested for loop example

# initialSalesGoal = 20000
# multiplier = 100
# offMonth = True

# for monthlyGoal in range(1, 13):
#     if monthlyGoal == 6 and offMonth:
#         print("Holiday month, no goals for month 6.")
#         continue
#     monthlySalesGoal = initialSalesGoal + (monthlyGoal * multiplier)
#     print("Your sales goal for the month " + str(monthlyGoal) + " is " +
#           str(monthlySalesGoal))  # str(converting numberic values to strings here)
#     for weeklyGoal in range(1, 5):
#         print("Your goal for the week " + str(weeklyGoal) +
#               " is " + str(monthlySalesGoal/4))
# print("Good luck with your sales.")

###################################################################################################

a = "40.6"
b = "60.4"

c = a + b
print(c)
