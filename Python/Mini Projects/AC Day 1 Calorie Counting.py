file = open("Python/Mini Projects/AC Day 1 Calorie Counting.txt","r")
fileList=list()
for x in (file):
    fileList.append(x.rstrip())
maxCal1=0
maxCal2=0
maxCal3=0
calCount =0
for y in fileList:
    if y=='':
        calCount=0
    else:
        indivCalCount=int(y)
        calCount+=indivCalCount
    if calCount > maxCal1:
        maxCal1=calCount
    elif calCount > maxCal2:
        maxCal2=calCount
    elif calCount > maxCal3:
        maxCal3=calCount
print("First: ",maxCal1,"Second: ",maxCal2,"Third: ",maxCal3)
totalCal=(maxCal1+maxCal2+maxCal3)
print("Total: ",totalCal)
