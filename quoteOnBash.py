import requests
r = requests.get('http://quotes.stormconsultancy.co.uk/random.json') 
quote = r.json()
print(quote["quote"])