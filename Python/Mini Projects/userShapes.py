import turtle
jeffrey=turtle.Turtle()
jeffrey.shape("turtle")

jeffrey.pencolor("black")
jeffrey.pensize(200000)
jeffrey.forward(1)
jeffrey.pensize(1)
jeffrey.pencolor("white")
jeffrey.speed(1000000000000000000000000000)
answer=input("What shape would you like to draw? ")
if answer == "circle" :
    for circle in range (360):
        jeffrey.forward(1)
        jeffrey.left(1)


if answer == "square" :
    for square in range (4):
        jeffrey.forward(50)
        jeffrey.left(90)


if answer == "sugar rush" :
    for sugar_rush in range (1000):
            print("You found an easter egg")
            jeffrey.speed(1000000000000000000000000000)
            jeffrey.forward(50)
            jeffrey.left(90)
            jeffrey.forward(50)
            jeffrey.left(90)
            jeffrey.forward(50)
            jeffrey.left(90)
            jeffrey.forward(50)

if answer == "triangle" :
    for triangle in range (3):
            jeffrey.forward(50)
            jeffrey.left(120)


if answer == "star" :
    for star in range (1):
        jeffrey.penup()
        jeffrey.right(35.5)
        jeffrey.forward(30)
        jeffrey.pendown()
        jeffrey.forward(70)
        jeffrey.left(135)
        jeffrey.forward(100)
        jeffrey.left(135)
        jeffrey.forward(100)
        jeffrey.left(135)
        jeffrey.forward(100)
        jeffrey.left(135)
        jeffrey.forward(100)
        jeffrey.left(135)
        jeffrey.forward(75)
else:
    print("You idiot, I can only draw four shapes, it's not that hard to pick one")



turtle.done()
