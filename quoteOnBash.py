import requests
try:
	r = requests.get('http://quotes.stormconsultancy.co.uk/random.json') 
	quote = r.json()
	print(quote["quote"])
except Exception as e:
	print "No quote for you because you deprived me of the internet. Haha."
