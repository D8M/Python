# Lessons from Class in GM

# annualMilesFlown = 420000
# region = "NorthWest"

# # if/elif statements always stop after 1st match --> put numbers in correct order.

# if annualMilesFlown >= 500000:
#     print("You are Gold level Customer")
               
# elif annualMilesFlown >= 400000:
#     print("You are Silver level Customer")
#     if region == "West":
#         print("Send a surfboard")
#     else:
#             print("Send a bycycle") 
# elif annualMilesFlown >= 200000:
#     print("You are Bronze level Customer")
# else:
#     print("Up and Coming Customer.")

# # NB: This line outide if statement --> not indented
# print("Thank you for flying with us.")

# annualMilesFlown = 420000
# region = "NorthWest"

# if/elif statements always stop after 1st match --> put numbers in correct order.
annualMilesFlown = 202000
newCustomer = True # Boolean var set to false here

if annualMilesFlown >= 500000:
    print("You are Gold level Customer")
               
elif annualMilesFlown >= 400000:
    print("You are Silver level Customer")

elif annualMilesFlown >= 200000 and newCustomer: # Here, nweCustomer is refering to itself becomes True
    print("You are Bronze level Customer and first time prize winner")
    
elif annualMilesFlown >= 200000:
    print("You are Bronze level Customer")
else:
    print("Up and Coming Customer.")

# NB: This line outide if statement --> not indented
print("Thank you for flying with us.")
