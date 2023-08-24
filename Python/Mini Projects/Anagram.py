# Get input from the user (variable: user)
user = str(input("enter your word: "))

#convert the input string to list (userList)
userList=list()
for x in user:
    userList.append(x)

# read the file
file = open("Python/Mini Projects/Words.txt","r")
# convert all the text in the file to a list (fileList)
fileList=list()
for x in (file):
    fileList.append(x.rstrip())
file.close()

fileListLen = list()
# Using a for loop to find the len of each individual word in fileList
for y in fileList:
	# if length of the word equal the length of the user input
    if len(user)==len(y):
     # append it into fileListLen
        fileListLen.append(y)



anagramList=[]
counter = 0

for a in fileListLen:
    counter=0
    for z in userList:
        if z in a.lower():
            counter=counter+1
    if counter==len(userList):
        anagramList.append(a.lower())

print(anagramList)
