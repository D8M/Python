import os

f = open("textfile.txt", "a")

for i in range(10,21):
    f.write("This is line: "  + str(i) + "\r\n")   
    

f.close()

filename = "textfile.txt"
print("Item exists: " + str(os.path.exists(filename)) )
print("Item is a File: " + str(os.path.isfile(filename)) ) # predicate function returns t/f
print("Item is a directory: " + str(os.path.isdir(filename)) )

if os.path.isfile(filename):
    f = open(filename, "r")
    lines = f.readlines() # Stores file contents as a list
    print(type(lines))

    for line in lines:
        print(line.strip()) # take away leading & trailing whitespace

    f.close()
else:
    print("File was not found :( ")

    
