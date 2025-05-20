#open the file
file = open ('accounts.txt')

#Read all the contents of the file, but once its already read it will stay at the bottom la
#file.read()

#Work around
#content = file.read(20)
#print (content)

#print some, by characters.
#print(file.read(3))

#Read single line at a time , Print by line
# byLine = file.readline()
# print (byLine)

#How to make it a loop, to read lines
# line = file.readline()
# while line != "":
#     print (line)
#     line = file.readline()

#Read and store in a list
for line in file.readlines():
    print (line)

#Close the file
file.close()