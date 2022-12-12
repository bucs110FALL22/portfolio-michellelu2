import requests

url = 'https://strangerthings-quotes.vercel.app/api/quotes'
response = requests.get(url).json()
print (response)