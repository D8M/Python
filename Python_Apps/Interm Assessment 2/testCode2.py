

kitty = 500 # Store cash in kittty var
requests = [] # Create empty requests List


with open("C:\\Users\davdb\Desktop\Programming\Python\loan_requests.txt") as f:
    requests = f.readlines()
    [line.strip() for line in requests]

# remove new line characters
#requests = [x.strip() for x in requests]
requests = [eval(i) for i in requests] # Eval converts requests list strings, to ints.


for i in range(len(requests)): # For loop to iterate over requests list      
   kitty - requests[i]   # Subtract the requets from the kitty
   
   
   if kitty >= requests[i] : # If kitty greater than or equal to request
        print(requests[i], " - Paid!")           
        #f.append("Request of " + str(requests[i]) + "paid in full.")
        
   elif kitty <= requests[i] and kitty > 0: # If kitty less than or equal to request     
        print(requests[i], "request cannot be processed in full ","(Insufficient funds available)." ,
        " Amount paid: ",kitty,)         
        
        
   else:  # If kitty empty     
       print("Request of", requests[i]," is UNPAID!")
  
       
   kitty = kitty - requests[i]  # Update kitty variable here.
      

