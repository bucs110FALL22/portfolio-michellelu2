import turtle 
import random

window = turtle.Screen()
myturtle = turtle.Turtle()
myturtle.color('blue')
myturtle.shape('turtle')
myturtle.goto(0,0)

coinflip = ['heads' , 'tails']

random = random.choice(coinflip)

for i in random:
  print (i)




window.exitonclick()



