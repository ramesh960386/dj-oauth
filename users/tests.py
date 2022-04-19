# from django.test import TestCase
import requests
from requests.auth import HTTPBasicAuth


headers = {
    'Authorization': 'Bearer F6zztWGonDJwhFeYZAtpjMzhll6bDD'
}

client_id = "aY48TYMPKYyNw8Xlji30pBv4n9SFlVq4lT9s8yeW"
client_secret = "kSNGQEQkp0WAMKniqkmJ0QBnwrVqC9JV5k3WVYqnSxEjzrxLs5Ji6eSAAgaPV2cGodpAUsWVepkCiVi2YwPe4QXQd0GQH0luP08fUYsaWQE6ZhwMnPfDR4zOVbtRnFcu"

# curl -X POST -d "grant_type=password&username=<user_name>&password=<password>" -u"<client_id>:<client_secret>" http://localhost:8000/o/token/

def getToken(username, password):
    url = "http://localhost:8000/o/token/"
    data = {
        "username": username,
        "password": password,
        "grant_type":"password",
        "client_id":client_id,
        "client_secret":client_secret
    }
    response = requests.post(url=url, data = data)
    # response = requests.post(url, auth=(client_id, client_secret))
    # response = requests.post(url=url, data = data, verify=False, auth=HTTPBasicAuth(client_id, client_secret))
    print(response.json())


# curl -X POST -d "grant_type=refresh_token&refresh_token=<your_refresh_token>&client_id=<your_client_id>&client_secret=<your_client_secret>" http://localhost:8000/o/token/
def refreshToken(username, password):
    url = "http://localhost:8000/o/token/"
    data = {
        "username": username,
        "password": password,
        "grant_type":"refresh_token",
        "refresh_token":"262YqYgX4nGBOiR2q0rwqH5Rr5i6TK",
        "client_id":client_id,
        "client_secret":client_secret
    }
    response = requests.post(url=url, data = data)
    print(response.json())


# curl -H "Authorization: Bearer <your_access_token>" http://localhost:8000/users/
def get_all_users():
    url = 'http://localhost:8000/api/users/'
    # PARAMS = {'address':location}
    # r = requests.get(url = URL, params = PARAMS)
    r = requests.get(url=url, headers=headers)
    print(r.json())


def post_resource():
    url = 'http://localhost:8000/api/cart-items/'
    data = {
        "product_name": "POCO Mobile",
        "product_price": 2000.0,
        "product_quantity": 20
    }
    # r = requests.get(url, headers=headers)
    r = requests.post(url=url, headers=headers, data = data)

    print(r.json())


def get_single_resource(id):
    url = f'http://localhost:8000/api/cart-items/{id}'
    r = requests.get(url=url, headers=headers)
    print(r.json())


def put_single_resource(id):
    data = {
        "product_name": "Jio Mobile",
        "product_price": 2500.0,
        "product_quantity": 20
    }
    url = f'http://localhost:8000/api/cart-items/{id}'
    r = requests.put(url=url, headers=headers, data=data)
    print(r.json())


def delete_single_resource(id):
    url = f'http://localhost:8000/api/cart-items/{id}'
    r = requests.delete(url=url, headers=headers)
    print(r.json())


if __name__ == "__main__":
    # get_all_resources()
    # post_resource()
    # get_single_resource(8)
    # put_single_resource(7)
    # delete_single_resource(9)
    # getToken("test@gmail.com", "test")
    # refreshToken("test@gmail.com", "test")
    get_all_users()

