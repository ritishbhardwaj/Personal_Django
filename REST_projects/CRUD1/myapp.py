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
        'name':'Nimish',
        'roll':499,
        'city': "Ambarsar"
    }

    json_data = json.dumps(data)
    r=requests.post(url=URL,data = json_data)

    data=r.json()
    print(r)

# post_data()

def update_data():
    data = {
        'id':3,
        'name':'Rishab Pant Bro',
        'city': 'Pata nai'
    }

    json_data = json.dumps(data)
    r=requests.put(url=URL,data=json_data)

    res_data = r.json()
    print(res_data)

update_data()
    
def delete_data():
    data = {
        'id':2
    }

    json_data = json.dumps(data)
    r=requests.delete(url=URL,data=json_data)

    res_data = r.json()
    print(res_data)

# delete_data()