import json

import requests
from jsonschema import validate

url = "https://reqres.in/api/users"

payload = {
  "name": "morpheus",
  "job": "leader"
}


# response = requests.request("POST", url, data=payload)
def test_api():
  response = requests.post(url, data=payload)
  print(response.text)
  body = response.json()
  assert response.status_code == 201
  with open("post_user.json") as file:
    validate(body, schema=json.loads(file.read()))