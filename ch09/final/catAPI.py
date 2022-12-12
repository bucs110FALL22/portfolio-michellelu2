import requests

class CatAPI:
  def __init__(self):
    '''Initializes the API url to get random facts about cats.'''
    self.api_url = 'https://meowfacts.herokuapp.com/?'

  
  def get(self):
    '''Converts cat API into json and returns the 'data' data from the API if it exists.'''
    response = requests.get(self.api_url).json()
    result = response['data']
    if response.get('data'):
      return result
    else:
      return None

  
  def __str__(self):
    '''Converts the data into a string and returns that string.'''
    resultStr = f"{self.get()}"
    return resultStr
    