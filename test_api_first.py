import json
import time

import allure
import requests
from allure_commons.model2 import Attachment
from allure_commons.types import AttachmentType
from jsonschema import validate
from selene import browser, have, by

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
    with allure.step("Api request"):
        response = requests.get(url_2)
        allure.attach(body=response.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")
        allure.attach(body=json.dumps(response.json(), indent=4, ensure_ascii=True), name="Response", attachment_type=AttachmentType.JSON, extension="json")
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
url_3 = "https://demowebshop.tricentis.com/login"
email="a.a.ostrovskiy@mail.ru"
password=148888
payload_3 = {"Email":email, "Password":password}
def test_authorization_by_api():
    with allure.step("Open browser"):
        browser.open("https://demowebshop.tricentis.com/")
    with allure.step("Authorization by API"):
        response = requests.post(url_3, data=payload_3, allow_redirects=False)
        allure.attach(body=response.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")
        allure.attach(body=str(response.cookies), name="Cookies", attachment_type=AttachmentType.TEXT, extension="txt")
    print(response.text)
    print(response.cookies)
    print(response.status_code)
    with allure.step("Get cookie from API"):
        cookie = response.cookies.get("NOPCOMMERCE.AUTH")
    with allure.step("Set cookie from API"):
        # browser.open("https://demowebshop.tricentis.com/")
        browser.driver.add_cookie({"name":"NOPCOMMERCE.AUTH", "value":cookie})
        browser.open("https://demowebshop.tricentis.com/")
    with allure.step("Assertion in terms of registration"):
        browser.all(".account").first.should(have.exact_text("a.a.ostrovskiy@mail.ru"))
    time.sleep(5)

def reqres_api_get(url, **kwargs):
    with allure.step("API Request"):
        response=requests.get(url=url, **kwargs)
        allure.attach(body=json.dumps(response.json(), indent=4, ensure_ascii=True),
                      name="Response", attachment_type=AttachmentType.JSON, extension="json")

def test_new():
    reqres_api_get("https://reqres.in/api/unknown/2")