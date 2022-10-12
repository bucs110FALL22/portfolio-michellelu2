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



#possible solution
# def star_pyramid():
#     levels = int(input("Enter the desired pyramid height: "))
#     for i in range(1, levels + 1):
#         print("*" * i)


# def rstar_pyramid():
#     levels = int(input("Enter the desired pyramid height: "))
#     for i in range(levels, 0, -1):
#         print("*" * i)


# star_pyramid()
# rstar_pyramid()