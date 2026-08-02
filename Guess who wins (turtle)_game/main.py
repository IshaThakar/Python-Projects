from turtle import Turtle,Screen
tim=Turtle()
screen = Screen()
def fwd():
    tim.forward(5)
def back():
    tim.backward(5)
def anticlk():
    newhead=tim.heading()+10
    tim.setheading(newhead)
def clockwise():
    newhead=tim.heading()-10
    tim.setheading(newhead)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
screen.listen()
screen.onkey(fwd,'w')
screen.onkey(back,'s')
screen.onkey(anticlk,'a')
screen.onkey(clockwise,'d')
screen.onkey(clear,'c')









screen.exitonclick()