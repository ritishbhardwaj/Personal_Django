import requests
import json


URL= 'http://127.0.0.1:8000/v1/apis/'

def get_data(id :int  = None):
    data ={}
    headers={
        'content-Type':'application/json'
    }
    if id is not None:
        data = {'id':id}

    json_data = json.dumps(data)
    r=requests.get(url=URL,data = json_data,headers=headers)

    data  = r.json()
    print(data)



def post_data():
    data={
        'name':'ritish',
        'roll':122,
        'city': "amritsar"
    }

    headers={
        'content-Type':'application/json'
    }

    json_data = json.dumps(data)
    r=requests.post(url=URL,data = json_data,headers=headers)

    data=r.json()
    print(data)


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

    
def delete_data():
    data = {
        'id':2
    }

    json_data = json.dumps(data)
    r=requests.delete(url=URL,data=json_data)

    res_data = r.json()
    print(res_data)

# delete_data()
post_data()
get_data()
# update_data()