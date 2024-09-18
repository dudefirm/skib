from turtle import Turtle, exitonclick


def baton():
    bob = Turtle()
    bob.speed(0)
    bob.color("#1a08ef")
    bob.forward(180)
    bob.left(90)
    bob.forward(75)
    bob.left(90)
    bob.forward(100)
    bob.right(90)
    bob.forward(125)
    bob.left(90)
    bob.forward(100)
    bob.left(90)
    bob.forward(125)
    bob.right(90)
    bob.forward(125)
    bob.forward(180)
    bob.left(90)
    bob.forward(75)
    bob.left(90)
    bob.forward(325)
    bob.penup()
    bob.goto(80,200)
    bob.pendown()
    bob.right(100)
    bob.begin_fill()
    bob.color("#3426e1")
    bob.setheading(90)
    bob.circle(51,180)
    bob.end_fill()







if __name__ == "__main__":
    baton()
    exitonclick()