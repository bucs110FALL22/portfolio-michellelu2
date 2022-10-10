import turtle 
import random

window = turtle.Screen()
myturtle = turtle.Turtle()
myturtle.shape('turtle')

colors = ['red' , 'blue' , 'green']

myturtle.speed(0)

distance = 10
angle = 90

in_screen = True

while in_screen:
  coin = random.randrange(0,2)
  if coin == 0:
    myturtle.right(angle)
  else:
    myturtle.left(angle)
  myturtle.forward(distance)

  turtleX =  myturtle.xcor()
  turtleY =  myturtle.ycor()

  x_range = window.window_width()/2
  y_range = window.window_height()/2

  myturtle.color(colors[0])

  colors.append(colors.pop(0))

  if abs(turtleX) > x_range or abs(turtleY) > y_range:
    in_screen = False

window.bgcolor('pink')
window.exitonclick()