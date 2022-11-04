import rectangle

class Surface:
  def __init__(self, filename, x, y, h, w):
    self.rect = rectangle.Rectangle(x, y, h, w)
    self.image = filename

  def getRect(self):
    return self.rect

def main():
  surfaces = Surface("filename", 6, 7, 8, 9)
  rectangle = surfaces.getRect()
  print(rectangle)
main()