import json

import requests
from jsonschema import validate

from schemas import post_users

url = "https://reqres.in/api/users"

payload = {
  "name": "morpheus",
  "job": "leader"
}

def test_api_from_file():
  response = requests.post(url, data=payload)
  # response = requests.request("POST", url, data=payload)
  print(response.text)
  body = response.json()
  assert response.status_code == 201
  with open("post_user.json") as file:
    validate(body, schema=json.loads(file.read()))

def test_api_from_variable():
  response = requests.post(url, data=payload)
  # response = requests.request("POST", url, data=payload)
  print(response.text)
  body = response.json()
  assert response.status_code == 201
  validate(body, schema=post_users)