import pygame 
import random 
import math

#Part A
pygame.init()
screen = pygame.display.set_mode()
size = pygame.display.get_window_size()
print("The screen size is:" , size)

screen_width = 250
screen_height = 250
screen = pygame.display.set_mode([screen_width , screen_height])

screen.fill('skyblue1')
pygame.draw.circle(screen, ('chartreuse4'), (125,125), 125)
pygame.draw.line(screen, ('black'), (125,0), (125,250), width=2)
pygame.draw.line(screen, ('black'), (0,125), (250,125), width=2)
pygame.display.flip()


#Part B
for i in range(10):
  x = random.randrange (0,251)
  y = random.randrange (0,251)
  coords = (x,y)

  distance_from_center = math.hypot(x-125, y-125) #the distance formula
  is_in_circle = distance_from_center <= 250/2 #screen width

  pygame.time.wait(500)
  
  if is_in_circle == True:
    pygame.draw.circle(screen, ('darkorange1'), coords, 5, 0)
  if is_in_circle == False:
    pygame.draw.circle(screen, ('midnightblue'), coords, 5, 0)

  pygame.display.flip()


#Part C
red_rect = pygame.draw.rect(screen, "red", [0, 0, 125, 250], 0)
blue_rect = pygame.draw.rect(screen, "blue", [125, 0, 125, 250], 0)
pygame.display.flip()
player_choice = ""
print ("Team Red or Team Blue?")

guess = True
while guess:
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
      if event.pos[0] < 125:
        player_choice = "red"
        guess = False

      elif event.pos[0] > 125:
        player_choice = "blue"
        guess = False
        
print ("You have chosen" , player_choice)
pygame.display.flip()
pygame.time.wait(500)

screen.fill('skyblue1')
pygame.draw.circle(screen, ('chartreuse4'), (125,125), 125)
pygame.draw.line(screen, ('black'), (125,0), (125,250), width=2)
pygame.draw.line(screen, ('black'), (0,125), (250,125), width=2)
pygame.display.flip()

for i in range(10):
  red_score = 0
  blue_score = 0

  print ("Red's turn")
  
  x = random.randrange (0,251)
  y = random.randrange (0,251)

  distance_from_center = math.hypot(x-125, y-125) 
  is_in_circle = distance_from_center <= 250/2 
  pygame.time.wait(500)
  
  if is_in_circle == True:
    pygame.draw.circle(screen, ('khaki1'), [x,y], 5, 0)
    print ("red hits")
    red_score += 1
  else:
    pygame.draw.circle(screen, ('tomato2'), [x,y], 5, 0)
    print ("red missed")
    red_score -= 1

  pygame.display.flip()

  x = random.randrange (0,251)
  y = random.randrange (0,251)

  print ("Blue's turn")
  distance_from_center = math.hypot(x-125, y-125) 
  is_in_circle = distance_from_center <= 250/2 
  pygame.time.wait(500)

  if is_in_circle == True:
    pygame.draw.circle(screen, ('khaki1'), [x,y], 5, 0)
    print ("blue hits")
    blue_score += 1
  else:
    pygame.draw.circle(screen, ('tomato2'), [x,y], 5, 0)
    print ("blue missed")
    blue_score -= 1
    
  pygame.display.flip()
  pygame.time.wait(500)

if player_choice == red_rect and red_score > blue_score:
  print ("Congradulations! You are correct.")

elif red_score < blue_score:
  print ("You lost. Better luck next time...")

else:
  print ("It's a tie.")