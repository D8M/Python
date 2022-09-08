#with open("C:\\Users\davdb\Desktop\Programming\Python\loan_requests.txt") as f:
#    requests = f.readlines() # Opens & creates file
f = open('C:\\Users\davdb\Desktop\Programming\Python\loan_requests.txt', 'r')
requests = f.readlines()
f.close()

f = open('C:\\Users\davdb\Desktop\Programming\Python\loan_requests.txt', 'r+')
f.seek(0)

print(requests)
requests = [x.strip() for x in requests]
requests = [line.strip('\n') for line in f]
print(requests)

requests = [eval(i) for i in requests] # Converts requests to intsz
#print(all([isinstance(item, int) for item in requests]))
 
# remove new line characters
#requests = [x.strip() for x in requests]
#requests = [line.strip('\n') for line in f]
#print(requests)
#requests = [eval(i) for i in requests] # Converts requests to intsz

#requests = [int(i) for i in requests]

#for i in range(0, len(requests)):
#    requests[i] = int(requests[i])
