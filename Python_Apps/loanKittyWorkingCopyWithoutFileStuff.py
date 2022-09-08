

kitty = 500 # Store cash in kittty var
requests = [] # Create empty requests List
remaining_total = 0 # Var

#with open("C:\\Users\davdb\Desktop\Programming\Python\loan_requests.txt") as f:
#    requests = f.readlines() # Opens & creates file
f = open('C:\\Users\davdb\Desktop\Programming\Python\loan_requests.txt', 'r')
requests = f.readlines()


# remove new line characters
requests = [x.strip() for x in requests]
#print(requests)
requests = [eval(i) for i in requests] # Converts requests to intsz
print(kitty)

for i in range(len(requests)):    
    kitty = kitty - requests[i] 
    #print(kitty)
      
    if kitty > 0 and kitty > requests[i] :
      print("Request of ", requests[i], "paid in full.")
      # Append to loan text file, see notes
      
    elif requests[i] >= kitty and kitty > 0:      
      print("Request of ", requests[i], " could not be paid in full." +
            "Partial payment of ", kitty % requests[i]   ," made")
       # Append to loan text file, see notes
     
    elif kitty == 0:
      print("Outstanding Request: ", requests[i])
      # Append to loan text file, see notes
      

      
      

      
  


      









