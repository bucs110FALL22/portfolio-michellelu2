import pygame

pygame.init()
pygame.font.init()

def collatzSequence(n):
  n = 101 
  
  upper_limit = 20
  iters = {}

  for i in range (2, upper_limit):
    count = 0

    while n > 1:
      if n % 2 == 0:
        n = n // 2

      else:
        n = n * 3 + 1

      count = count + 1
      iters [n] = count 

      print ("number: " , n)
      print ("count: " , count)
      print ("iterations: " , iters)


screenWidth = 400
screenHeight = 400
window = pygame.display.set_mode([screenWidth , screenHeight])
window.fill('aliceblue')


pygame.time.wait(500)
pygame.draw.line(window, ('black'), (200,0), (200,400), width = 2)
pygame.draw.line(window, ('black'), (0,200), (400,200), width = 2)

pygame.display.flip()

collatzSequence(2)