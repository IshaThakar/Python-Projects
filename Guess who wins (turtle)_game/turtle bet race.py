from turtle import Turtle,Screen
import random
screen = Screen()
screen.setup(500,400)
ubet=screen.textinput(prompt="Which turtle will win the race?? Enter a colour:",title="MAKE YOUR BET!!")
print(ubet)
color=['red','yellow','blue','green','purple','cyan']
y_pos=[0,30,60,90,-30,-60]
step=[10,5,20,30,50,2]
all_turtles=[]
is_race_on=False
for turtle_index in range(0,6):
 tim=Turtle()
 tim.color(color[turtle_index])
 tim.shape('turtle')
 tim.penup()
 tim.goto(-230,y_pos[turtle_index])
 all_turtles.append(tim)
if ubet:
    is_race_on=True
while is_race_on:
 for turtle in all_turtles:
   if turtle.xcor()>230:
       is_race_on=False
       win_colour=turtle.pencolor()
       if win_colour== ubet :
           print(f"YOU WIN!!!the winner is {win_colour}")
       else:
           print(f"YOU LOSE!!!the winner is {win_colour}")

   turtle.forward(random.choice(step))

screen.exitonclick()