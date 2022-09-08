

kitty = 500 # Store cash in kittty var
requests = [] # Create empty requests List
remaining_total = 0 # Var

#with open("C:\\Users\davdb\Desktop\Programming\Python\loan_requests.txt") as f:
#    requests = f.readlines() # Opens & creates file
f = open('C:\\Users\davdb\Desktop\Programming\Python\loan_requests.txt', 'r')
requests = f.readlines()
f.close()

f = open('C:\\Users\davdb\Desktop\Programming\Python\loan_requests.txt', 'r+')
f.seek(0)

#print(requests)
requests = [x.strip() for x in requests]
requests = [line.strip('\n') for line in f]
#print(requests)

requests = [eval(i) for i in requests] # Converts requests to intsz
print(all([isinstance(item, int) for item in requests]))
# remove new line characters

#requests = [x.strip() for x in requests]
#requests = [line.strip('\n') for line in f]
#print(requests)
#requests = [eval(i) for i in requests] # Converts requests to intsz
#print(requests[i].isdigit())
#requests = [int(i) for i in requests]

#for i in range(0, len(requests)):
#    requests[i] = int(requests[i])
#print(kitty)

for i in range(len(requests)):    
    kitty = kitty - requests[i] 
    #print(kitty)
      
    if kitty > 0 and kitty > requests[i] :
      print("Request of ", int(requests[i]), "paid in full.")
      
      
    elif requests[i] >= kitty and kitty > 0:      
      print("Request of ", int(requests[i]), " could not be paid in full." +
            "Partial payment of ", kitty % requests[i]   ," made")      
       # Append to loan text file, see notes
     
    elif kitty == 0:
      print("Outstanding Request: ", requests[i])
      # Append to loan text file, see notes

   #############################################

    i

    #print(f.read())   
    #f.seek(0)
    #requests = [line.rstrip('\n') for line in f]
    #print("This is requests", requests)
      

      
  #f = open('C:\\Users\davdb\Desktop\Programming\Python\loan_requests.txt', 'a+')
     #     f.write('\n'.join(["\nRequest of " + str(requests[i]) + " paid in full"]))
     #     f.close


      









