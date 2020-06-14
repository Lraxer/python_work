import requests
import json

def showchain():
	url1 = "http://localhost:5000/showchain"
	url2 = "http://localhost:5001/showchain"
	return requests.get(url1)

def add_transactions():
	url = "http://localhost:5000/transactions/new"
	data = {
		"start": "123456",
		"end": "someone",
		"amount": 5
	}
	data = json.dumps(data)
	return requests.post(url=url, data=data)

def mine():
	url = "http://localhost:5000/mine"
	return requests.get(url)

def addnei():
	nei1 = "http://127.0.0.1:5000"
	nei2 = "http://127.0.0.1:5001"
	url1 = "http://127.0.0.1:5000/neighbor/register"
	url2 = "http://127.0.0.1:5001/neighbor/register"
	data = {
		"neighbor": [nei1],
	}
	data = json.dumps(data)
	return requests.post(url2, data=data)

def solve():
	url1 = "http://127.0.0.1:5000/neighbor/solve"
	url2 = "http://127.0.0.1:5001/neighbor/solve"
	return requests.get(url2)


if __name__ == "__main__":
	# res = showchain()
	# res = add_transactions()
	# res = mine()
	# res = addnei()
	# res = solve()
	print(res.text)