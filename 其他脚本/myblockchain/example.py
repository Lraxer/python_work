import requests
import json

def showchain():
	url = "http://localhost:5000/showchain"
	return requests.get(url2)

def add_transactions():
	url = "http://localhost:5000/transactions/new"
	data = {
		"start": "123456",
		"end": "someone",
		"amount": 5
	}
	data = json.dumps(data)
	return requests.post(url=url, data=data)\

def mine():
	url = "http://localhost:5000/mine"
	return requests.get(url)

if __name__ == "__main__":
	res = showchain()
	# res = add_transactions()
	# res = mine()
	print(res.text)