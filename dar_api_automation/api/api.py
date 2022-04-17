import curlify
import requests


class Api:
    host = None
    data_user = None

    def __init__(self, host):
        self.host = host

    def login(self):
        data = {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }
        headers_type = {"Content-Type": "application/json"}
        response = requests.post(self.host + "login", headers=headers_type, json=data, verify=False
                                 )
        print("\n" + curlify.to_curl(response.request, compressed=True))
        print("\n" + response.text)
        return response

    def register(self):
        data = {
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        }
        headers_type = {"Content-Type": "application/json"}
        response = requests.post(self.host + "register", headers=headers_type, json=data,
                                 verify=False)
        print(curlify.to_curl(response.request, compressed=True))
        print(response.text)
        return response

    def create_user(self):
        data = {

                "name": "morpheus",
                "job": "leader"

        }
        headers_type = {"Content-Type": "application/json"}
        response = requests.post(self.host + "users", headers=headers_type, json=data, verify=False
                                 )
        print("\n" + curlify.to_curl(response.request, compressed=True))
        print("\n" + response.text)
        return response

    def list_of_users(self):
        headers_type = {"Content-Type": "application/json"}
        response = requests.get(self.host + "users?page=2", headers=headers_type, verify=False
                                 )
        print("\n" + curlify.to_curl(response.request, compressed=True))
        print("\n" + response.text)
        return response

