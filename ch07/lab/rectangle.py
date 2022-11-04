class Rectangle:
  
  def __init__(self, x, y, h, w):
    self.x = max(0,x)
    self.y = max(0,y)
    self.height = max(0,h)
    self.width = max(0,w)

  def __str__(self):
    str_result = f"coordinate:{self.x , self.y}"
    str_result += f"\nheight:{self.height}"
    str_result += f"\nwidth:{self.width}"
    return str_result

def main():
  rectangles= Rectangle(9, 16, 25, 38)
  print(rectangles)
main()