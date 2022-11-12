class StringUtility:

  def __init__(self, string):
    self.string = string

  def __str__(self):
    return self.string

  

  def vowels(self):
    count = 0
    for i in self.string:
      if (i=='a' or i=='e' or i=="i" or i=="o" or i=="u"):
        count = count + 1

    if count >= 5:
      return f"many"
      
    else:
      return str(count)


  
  def bothEnds(self):
    if len(self.string) >= 2:
      myString = self.string[0] + self.string[1] + self.string[-2] + self.string[-1]
      return myString

    else:
      return ''

      
  
  def fixStart(self):
    if len(self.string) >= 1:
      char = self.string[0]
      for i in self.string:
        myString = self.string[1: ].replace(char, '*')
      return self.string[0] + myString

    else:
      return ''
        


  def asciiSum(self):
    ascii_sum = 0
    for i in self.string:
      ascii_sum += ord(i)
    return ascii_sum