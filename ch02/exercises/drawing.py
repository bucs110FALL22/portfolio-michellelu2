import turtle
my_turtle = turtle.Turtle()
window = turtle.Screen()
my_turtle.color("blue")
my_turtle.shape("turtle")
sides = int(input("Number of sides: "))
length = int(input("Length of each side: "))
for i in range(sides):
  my_turtle.left(360/sides)
  my_turtle.forward(length)
window.exitonclick()