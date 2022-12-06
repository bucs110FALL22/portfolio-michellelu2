class StringUtility:

  def __init__(self, string):
    '''Take a string as a perimeter and stores it as an instance variable.'''
    self.string = string

  
  def __str__(self):
    '''Return the internal string unchanged.'''
    result = self.string
    return result


  def vowels(self):
    '''
    Count the number of vowels in a string and return <count>.
    If <count> is 5 or more, then return the word 'many'.
    '''
    count = 0
    for i in self.string:
      if (i=='a' or i=='e' or i=="i" or i=="o" or i=="u"):
        count = count + 1
    if count >= 5:
      return f"many"
    else:
      return str(count)

  
  def bothEnds(self):
    '''Return a string made of the first 2 and last 2 characters of the original string.'''
    if len(self.string) >= 2:
      myString = self.string[0] + self.string[1] + self.string[-2] + self.string[-1]
      return myString
    else:
      return ''
      
  
  def fixStart(self):
    '''
    Return a string where all occurrences of its first character have been changed to '*'.
    Do not change the first character.
    '''
    if len(self.string) >= 1:
      char = self.string[0]
      for i in self.string:
        myString = self.string[1: ].replace(char, '*')
      return self.string[0] + myString
    else:
      return ''
        

  def asciiSum(self):
    '''Return an integer that is the sum of all ascii values in the string.'''
    ascii_sum = 0
    for i in self.string:
      ascii_sum += ord(i)
    return ascii_sum


  def cipher(self):
    '''Returns a string where each character is shifted by the length of the string and accounting for uppercase or lowercase letters.'''
    shift = len(self.string)
    result = ""
    for i in range(shift):
      char = self.string[i]
      if char.islower():
        value1 = (((((ord(char)) - 97) + shift) % 26) + 97)
        result += chr(value1)
      elif char.isupper():
        value2 = (((((ord(char)) - 65) + shift) % 26) + 65)
        result += chr(value2)
      else: 
        result += self.string[i]
    return result