kitty = 500 # Store cash in kittty var
requests = [] # Create empty requests List
temp = [] # Var

with open("C:\\Users\davdb\Desktop\Programming\Python\loan_requests.txt") as f:
    requests = f.readlines() # Opens & creates file 

# remove new line characters
requests = [x.strip() for x in requests]
#print(requests)
requests = [eval(i) for i in requests] # Converts requests to ints
print(kitty)

for i in range(len(requests)):    
        kitty = kitty - requests[i]
        print(kitty)





        


        #if  kitty > requests[i] :
        #  print(requests[i], " - Paid!")
        # Append to loan text file, see notes
      
        #elif kitty <= requests[i]  :
         #print(requests[i], " request cannot be processed in full (Insuffucent funds available)." +
         # " Amount paid: ", kitty    ,"Kitty is now ",kitty)
          # Append to loan text file, see notes
     
        #else: 
         # print("Outstanding Request: ", requests[i])
          # Append to loan text file, see notes
          

      
