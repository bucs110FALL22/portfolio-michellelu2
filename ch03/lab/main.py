import turtle #1. import modules
import random
import pygame 
import math

#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. Your PART A code goes here
# Race 1
window.delay(100)

michelangelo.down()
leonardo.down()

michelangelo.forward(random.randrange(1,101))
leonardo.forward(random.randrange(1,101))

michelangelo.clear()
leonardo.clear()

michelangelo.up()
leonardo.up()

michelangelo.hideturtle()
leonardo.hideturtle()

michelangelo.speed(5)
leonardo.speed(5)

michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

michelangelo.showturtle()
leonardo.showturtle()

#Race 2
michelangelo.down()
leonardo.down()

for i in range(10):
  michelangelo.forward(random.randrange(0,11))
  leonardo.forward(random.randrange(0,11))

michelangelo.clear()
leonardo.clear()

michelangelo.up()
leonardo.up()

michelangelo.goto(-100,20)
leonardo.goto(-100,-20)


# PART B - complete part B here
pygame.init()
window = pygame.display.set_mode()
window.fill('ghostwhite')
pygame.display.flip()

side_length = 50
offset = 100

num_sides = 3
coords = []
for i in range(num_sides):
  theta = (2.0 * math.pi * (i)) / num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append([x,y])

window.fill('ghostwhite')
pygame.display.flip()

pygame.draw.polygon(window, "blue", coords)
pygame.display.flip()
pygame.time.wait(1000)

window.fill('ghostwhite')
pygame.display.flip()

coords = []
num_sides = 4
for i in range(num_sides):
  theta = (2.0 * math.pi * (i)) / num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append([x,y])

pygame.draw.polygon(window, "brown", coords)
pygame.display.flip()
pygame.time.wait(1000)

window.fill('ghostwhite')
pygame.display.flip()

coords = []
num_sides = 6
for i in range(num_sides):
  theta = (2.0 * math.pi * (i)) / num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append([x,y])

pygame.draw.polygon(window, "brown", coords)
pygame.display.flip()
pygame.time.wait(1000)

window.fill('ghostwhite')
pygame.display.flip()

coords = []
num_sides = 9
for i in range(num_sides):
  theta = (2.0 * math.pi * (i)) / num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append([x,y])

pygame.draw.polygon(window, "coral", coords)
pygame.display.flip()
pygame.time.wait(1000)

window.fill('ghostwhite')
pygame.display.flip()

coords = []
num_sides = 360
for i in range(num_sides):
  theta = (2.0 * math.pi * (i)) / num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append([x,y])

pygame.draw.polygon(window, "darkgreen", coords)
pygame.display.flip()
pygame.time.wait(1000)

window.fill('ghostwhite')
pygame.display.flip()

window.exitonclick()