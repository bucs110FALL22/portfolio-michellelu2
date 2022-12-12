import requests

class WeatherAPI:
  def __init__(self, city):
    '''Initializes the API url to get a city's weather.'''
    self.city = city
    self.api_url = f"http://api.openweathermap.org/data/2.5/weather?q={self.city}&appid=580fefe2ba96d3847bc2bbc5bc70d14c"

  
  def get(self):
    '''Converts weather API into json and returns the 'temp' data from API if it exists.'''
    response = requests.get(self.api_url).json()
    result = response['main']['temp']
    if response.get('main'):
      return result
    else:
      return None

  
  def __str__(self):
    '''Converts the data into a string and returns that string.'''
    resultStr = f"{self.get()}"
    return resultStr
  