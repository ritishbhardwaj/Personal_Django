import requests
import json


URL= 'http://127.0.0.1:8000/v1/apis'

def get_data(id :int  = None):
    data ={}
    if id is not None:
        data = {'id':id}

    json_data = json.dumps(data)
    r=requests.get(url=URL,data = json_data)

    data  = r.json()
    print(data)

# get_data(1)


def post_data():
    data={
        'name':'ritish',
        'roll':122,
        'city': "amritsar"
    }

    json_data = json.dumps(data)
    r=requests.post(url=URL,data = json_data)

    data=r.json()
    print(data)

post_data()

def update_data():
    data = {
        'id':10,
        'name':'Rishab Pant Bro',
        'city': 'Dholakpur'
    }

    json_data = json.dumps(data)
    r=requests.put(url=URL,data=json_data)

    res_data = r.json()
    print(res_data)

# update_data()
    
def delete_data():
    data = {
        'id':2
    }

    json_data = json.dumps(data)
    r=requests.delete(url=URL,data=json_data)

    res_data = r.json()
    print(res_data)

# delete_data()