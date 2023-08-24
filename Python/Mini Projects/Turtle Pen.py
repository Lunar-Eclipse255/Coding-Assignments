
import turtle
jeffrey=turtle.Turtle()
jeffrey.shape("turtle")

jeffrey.pencolor("black")
jeffrey.pensize(200000)
jeffrey.forward(1)
jeffrey.pensize(1)
jeffrey.pencolor("white")
jeffrey.speed(100000000000000000000)
answer=input("Where would you like to go ")
    
while answer!= "stop":
    answer=input("")
    if answer == "w":
        jeffrey.forward(10)
    if answer == "s":
        jeffrey.backward(10)
    if answer == "a":
        jeffrey.left(90)
    if answer == "d":
        jeffrey.right(90)
    if answer =="c":
        jeffrey.pencolor("black")
        jeffrey.pensize(20000)
        jeffrey.forward(1)
        jeffrey.backward(1)
        jeffrey.pencolor("white")



#import turtle
#copy beginning code from Shapes.py
#program if statements for w,and s make them move 5 pixels for each,
#for a, and d make them turn in their respective directions 90º with if statements,
#program c,and q to clear the screen and quit using if statements. Have the user to be able to do letter/number commands until they click q
#add turns that take user input to turn
#add the code that keeps the turtle on the screen.
