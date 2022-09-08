print("Enter the Name of File: ")
fileName = str(input())
fileHandle = open(fileName, "a")
print("Enter the Text to Append in Given File: ")

while True:
    text = str(input())
    if len(text)>0:
        fileHandle.write("\n")
        fileHandle.write(text)
    else:
        break
    
#fileHandle = open('C:\\Users\\davdb\\Desktop\\Programming\\Python\\Python_Projects\\edit.txt','r')
#fileHandle.close()

fileHandle = open(fileName, "r")
for content in fileHandle:
      print(end=content)
fileHandle.close()
