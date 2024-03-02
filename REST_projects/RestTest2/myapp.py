import requests,json

URL ="http://127.0.0.1:8000/ta/stucreate"


data = {
    'name' : 'Sonam',
    'roll' : 101 , 
    'city' : 'Ranchi'
}

json_data=json.dumps(data)

print(json_data , "#######################")

r=requests.post(url=URL,json=json_data)

data = r.json()
print(data)
