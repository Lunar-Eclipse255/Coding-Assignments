#Assigns the List
List=[57,12,-5,32,65,0,15,1,90,72]
#Prints the numbers all on the same line
print(List)

#Prints every number on a different line
for numbers in range(len(List)):
    print(List[numbers])

#Finds the even numbers
Mod1=List[0]%2
Mod2=List[1]%2
Mod3 = List[2]%2
Mod4 = List[3]%2
Mod5 = List[4]%2
Mod6 = List[5]%2
Mod7 = List[6]%2
Mod8 = List[7]%2
Mod9 = List[8]%2
Mod10 = List[9]%2
print("The even numbers are:")
if Mod1==0:
    print(List[0])
    Mod1 == True
if Mod2==0:
    Mod2 == True
    print(List[1])
if Mod3==0:
    Mod3 == True
    print(List[2])
if Mod4==0:
    Mod4 == True
    print(List[3])
if Mod5==0:
    Mod5 == True
    print(List[4])
if Mod6==0:
    Mod6 == True
    print(List[5])
if Mod7==0:
    Mod7 == True
    print(List[6])
if Mod8==0:
    Mod8 == True
    print(List[7])
if Mod9==0:
    Mod9 == True
    print(List[8])
if Mod10==0:
    Mod10 == True
    print(List[9])

#Finds the largest number
largest = -1000000000000000000000000000
for num in List:
    if num>largest:
        largest=num
print(largest, "is the largest number.")

#Finds the smallest number
smallest = 1000000000000000000000000000
for num2 in List:

    if num2<smallest:
        smallest=num
print(smallest, "is the smallest number.")

#Finds the average
average=(List[0]+List[1]+List[2]+List[3]+List[4]+List[5]+List[6]+List[7]+List[8]+List[9])/len(List)
print(average)
