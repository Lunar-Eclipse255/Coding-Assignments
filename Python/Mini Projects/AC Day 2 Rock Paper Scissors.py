file = open("Python/Mini Projects/AC Day 2 Rock Paper Scissors.txt","r")
counter=0
fileList=list()
for x in (file):
    fileList.append(x.rstrip())
for y in fileList:
    if y=='A X':
        counter=counter+3
    elif y=='A Y':
        counter=counter+4
    elif y=='A Z':
        counter=counter+8
    elif y=='B X':
        counter=counter+1
    elif y=='B Y':
        counter=counter+5
    elif y=='B Z':
        counter=counter+9
    elif y=='C X':
        counter=counter+2
    elif y=='C Y':
        counter=counter+6
    elif y=='C Z':
        counter=counter+7
print(counter)
