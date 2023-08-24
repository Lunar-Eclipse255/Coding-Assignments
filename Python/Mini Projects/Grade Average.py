grade=0
total=0
numGrades=0
print("Put negative number to stop")
grade = float(input("What was your grade? "))
while grade >= 0:
    numGrades=numGrades+1
    total=grade+total
    grade = float(input("What was your grade? "))

print("Your grade average was ", total/numGrades, "%")
