import requests
import json


ENDPOINT ="http://127.0.0.1:8000/api/status/"


def do(method ='get', data={}, is_json =True):
    headers = {}
    if is_json:
        headers['content-type'] ='application/json'
        data = json.dumps(data)
    r = requests.request(method, ENDPOINT, data=data, headers = headers )
    print(r.text)
    print(r.status_code)
    return r
"""
CRUD IS READY
"""
do(data={'id':15})  #retrive
#do(method='post', data={"content": "some cool api ", 'user':1}) # create
#do(method='put', data={"id":15, "content": "some cool api walker to mumbai ", 'user':1}) #update
#do(method='delete', data={"id":13}) #delete
