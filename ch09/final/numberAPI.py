import requests

class NumberAPI:
  def __init__(self):
    '''Initializes the API url to get random number facts.'''
    self.api_url = 'http://numbersapi.com/random/trivia?json'

  
  def get(self):
    '''Converts number API into json and returns the 'text' data from API if it exists.'''
    response = requests.get(self.api_url).json()
    result = response['text']
    if response.get('text'):
      return result
    else:
      return None

  
  def __str__(self):
    '''Converts the data into a string and returns that string.'''
    resultStr = f"{self.get()}"
    return resultStr
    