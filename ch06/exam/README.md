# CS110 Midterm Exam
import turtle 
import random

window = turtle.Screen()
my_turtle = turtle.Turtle()
window.bgcolor('black')
window.setup(500,300)


def star(size=4 , angle=120):
  my_turtle.color('yellow')
  my_turtle.speed(0)
  my_turtle.begin_fill()
  
  for i in range(5):
    my_turtle.forward(size)
    my_turtle.right(angle)
    my_turtle.forward(size)
    my_turtle.right(72 - angle)
    
  my_turtle.end_fill()
  return star

for i in range(40):
  x_coordinate = random.randint(-250 , 251)
  y_coordinate = random.randint(-140 , 151)
  star()
  my_turtle.penup()
  my_turtle.goto(x_coordinate , y_coordinate)
  my_turtle.pendown()


def trapezoid(color=None , x=0 , y=0):
  my_turtle.color(color)
  my_turtle.begin_fill()
  my_turtle.penup()
  my_turtle.goto(x , y)
  my_turtle.pendown()
  my_turtle.forward(120)
  my_turtle.right(55)
  my_turtle.forward(65)
  my_turtle.right(125)
  my_turtle.forward(190)
  my_turtle.right(125)
  my_turtle.forward(65)
  my_turtle.goto(x , y)
  my_turtle.end_fill()
  return trapezoid


def semicircle(color=None , x=0 , y=0 , radius=0 , degrees=0):
  my_turtle.color(color)
  my_turtle.begin_fill()
  my_turtle.penup()
  my_turtle.goto(x , y)
  my_turtle.pendown()
  my_turtle.right(55)
  my_turtle.forward(120)
  my_turtle.left(90)
  my_turtle.circle(radius , degrees)
  my_turtle.end_fill()
  return semicircle
  

def circle(color=None , x=0 , y=0 ,radius=0):
  my_turtle.color(color)
  my_turtle.begin_fill()
  my_turtle.penup()
  my_turtle.goto(x , y)
  my_turtle.pendown()
  my_turtle.circle(radius)
  my_turtle.end_fill()
  return circle
  

def rectangle(x=0 , y=0 , color=None , height=0 , width=0):
  my_turtle.color(color)
  my_turtle.begin_fill()
  my_turtle.penup()
  my_turtle.goto(x , y)
  my_turtle.pendown()
  my_turtle.forward(height)
  my_turtle.right(90)
  my_turtle.forward(width)
  my_turtle.right(90)
  my_turtle.forward(height)
  my_turtle.right(90)
  my_turtle.forward(width)
  my_turtle.end_fill()
  return rectangle
  

def rays(color=None , size=0):
  my_turtle.color(color)
  my_turtle.pensize(size)
  my_turtle.penup()
  my_turtle.goto(-60 , -60)
  my_turtle.pendown()
  my_turtle.goto(-90 , -110)
  my_turtle.penup()
  my_turtle.goto(0 , -60)
  my_turtle.pendown()
  my_turtle.goto(0 , -120)
  my_turtle.penup()
  my_turtle.goto(60 , -60)
  my_turtle.pendown()
  my_turtle.goto(90 , -110)
  return rays


def main():
  stars = star(size=4 , angle=120)
  print(stars)

  ufo_part1 = trapezoid(color='darkviolet' , x=-66 , y=0)
  print(ufo_part1)
  
  ufo_part2 = semicircle(color='royalblue' , x=-66, y=0 , radius=60 , degrees=180)
  print (ufo_part2)
  
  ufo_part3 = circle(color='white' , x=25 , y=19 , radius=8)
  print (ufo_part3)
  
  ufo_part4 = rectangle(x=40 , y=-15 , color='silver' , height=20 , width=90)
  print (ufo_part4)

  ufo_part5 = rays(color='limegreen' , size=7)
  print (ufo_part5)
  
main()

window.exitonclick()



## SHORT DESCRIPTION *(My program will illustrate a UFO against a starry background.)*


## KNOWN BUGS AND INCOMPLETE PARTS *(Nope)*

## REFERENCES *(Nope)*

## MISCELLANEOUS COMMENTS *(Nope)*