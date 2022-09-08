workFile = open('C:\\Users\\davdb\\Desktop\\LoremIpsum.txt','r')
workFileFirstLine = workFile.readline()
print(workFileFirstLine)

workFile.close()
print("File has  been closed")
