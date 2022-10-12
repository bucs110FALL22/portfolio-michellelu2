import turtle 

window = turtle.Screen()

def drawEqShape(myturtle=None, num_sides=0 , side_length=0):
  num_sides = int(input("Number of sides: "))
  side_length = int(input("Length of each side: "))
  for i in range(num_sides):
    myTurtle.left(360/num_sides)
    myTurtle.forward(side_length)

myTurtle = turtle.Turtle()
myTurtle.shape("turtle")
myTurtle.color("green")
drawEqShape(myTurtle, 1, 1)

window.exitonclick()