def star_pattern():
  rows = int(input("Enter a number: "))
  for i in range(rows):
    print ("*" * (i+1))
    
star_pattern()

    
def rstar_pyramid():
  rows = int(input("Enter a number: "))
  for i in reversed(range(rows)):
    print ("*" * (i + 1))

rstar_pyramid()