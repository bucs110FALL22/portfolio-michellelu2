from weatherAPI import WeatherAPI
from catAPI import CatAPI
from numberAPI import NumberAPI

def controller():
  '''Returns the temperature in a specific city and also returns either a random cat fact or number fact depending on the temperature.'''

  userInput = input("Enter a City: ")

  weather = WeatherAPI(userInput)
  kelvin = str(weather)
  catFact = CatAPI()
  numberFact = NumberAPI()

  celsius = (int(float(kelvin))) - 273.15
  fahrenheit = round(celsius * (9/5) + 32)

  if fahrenheit >= 50:
    print (f"Today's temperature in {userInput} is {fahrenheit}° Fahrenheit. Here is a fun fact about cats to better your day: {catFact}")
  if fahrenheit < 50:
    print (f"Today's temperature in {userInput} is {fahrenheit}° Fahrenheit. Here is an extremely interesting and useful number-related fact to know: {numberFact}")
    