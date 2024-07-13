import json

import allure
import requests
from jsonschema import validate

from schemas import post_users, post_user_2

url = "https://reqres.in/api/users"
name="Alex"
job="Ingineer"
payload = {
  "name": name,
  "job": job
}
@allure.link("https://reqres.in", name="Testing API")
@allure.step("First try")
def test_api_from_file():
    with allure.step("Get response"):
        response = requests.post(url, data=payload)
  # response = requests.request("POST", url, data=payload)
    print(response.text)
    body = response.json()
    with allure.step("Assertion"):
        assert body["name"] == name
        assert body["job"] == job
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

url_2="https://reqres.in/api/unknown/2"
payload_2= {}
def test_api_from_file_2():
    response = requests.get(url_2, data=payload_2)
    print(response.text)
    body = response.json()
    assert response.status_code == 200
    with open("post_user_2.json") as file:
        validate(body, schema=json.loads(file.read()))

def test_api_from_variable_2():
    response = requests.get(url_2)
    print(response.text)
    body = response.json()
    assert body["data"]["name"] == "fuchsia rose"
    assert response.status_code == 200
    validate(body, schema=post_user_2)

def test_api_with_params():
    response = requests.post(url, data=payload, params={"page":3}, verify=False)
    # response = requests.request("POST", url, data=payload)
    print(response.text)
    body = response.json()
    assert body["name"] == name
    assert body["job"] == job
    assert response.status_code == 201
    with open("post_user.json") as file:
        validate(body, schema=json.loads(file.read()))