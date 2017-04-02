import requests
try:
	r = requests.get('http://quotes.rest/qod.json?category=inspire') 
	quote = r.json()
	# print(quote)
	print(quote["contents"]["quotes"][0]["quote"],end=" \t\t\t\t "),
	print(quote["contents"]["quotes"][0]["author"])
except Exception as e:
	print ("No internet")
