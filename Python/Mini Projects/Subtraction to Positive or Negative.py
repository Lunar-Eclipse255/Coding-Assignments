num1=int(input("Give me a number to subtract "))
num2=int(input("Give me another number "))
def difference (num1, num2):
    answer=num1-num2
    return(answer)
answer=difference(num1,num2)
if answer >0:
    print("Your answer is positive")
if answer==0:
    print("Your answer is 0")
if answer<0:
    print("Your answer is negative")
