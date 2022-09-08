

with open('C:\\Users\\davdb\\Desktop\\LoremIpsum.txt') as workFile:
    workFileContents = workFile.readlines()
    while workFileContents:
        print(workFileContents)
        workFileContents = workFile.readlines()

print(workFileContents)
print("File has  been closed")
print(workFileContents.fileno())


