import requests
import os
import time


class WebStore:
    def __init__(self, name, url, path=None):
        self.name = name
        self.url = url
        self.path = path if path else os.getcwd()

    def validate_url(self, url):
        response = self.send_request_safe(url)

        if response.status_code == 200:
            return url
        else:
            raise ValueError("Wrong url")

    @staticmethod
    def send_request_safe(url):
        while True:
            try:
                return requests.get(url)
            except requests.exceptions.ConnectionError:
                time.sleep(2)
                continue
            except Exception as err:
                raise Exception("something wrong has happened {}".format(err))


class ClothesStore(WebStore):
    def __init__(self, women, men):
        super().__init__(women, men)
        self.women = women
        self.men = men


class OnlineOrders(ClothesStore):
    def __init__(self, online_order_id, item_name):
        super().__init__(online_order_id, item_name)
        self.online_order_id = online_order_id
        self.item_name = item_name


class Client:
    def __init__(self, full_name_client, id_client, phone, address, username, email, password):
        self.full_name_client = full_name_client
        self.id_client = id_client
        self.phone = phone
        self.address = address
        self.username = username
        self.email = email
        self.password = password

    @staticmethod
    def ordered_product(address):
        dict_ = {}
        for address in range(1, address+1):
            dict_[f"address_{address}"] = "added"
        address_ = count(dict_)
        

def file_name_generator():
    while True:
        try:
            response = requests.get(url)
        except requests.exceptions.ConnectionError:
            time.sleep(5)
            continue

        if response.status_code == 200:
            data = response.json()
        else:
            raise Exception("something went wrong")

        file_name = data.get("results")[0].get("login").get("username")

        yield file_name


neworder_1 = "Customer name is: George william Bill" + "\n" + "Order_id: 232136146" + "\n" + "Address : 123455"
neworder_2 = "Customer name is: Sue John Joe" + "\n" + "Order_id:232136146" + "\n" + "Address : 136546"
neworder_3 = "Customer name is: John Jack Joe" + "\n" + "Order_id:23459874" + "\n" + "Address : 136546"
neworder_4 = "Customer name is: Bill Jack Joe" + "\n" + "Order_id:23459885" + "\n" + "Address : 136546"
neworder_5 = "Customer name is: Sam william Bill" + "\n" + "Order_id: 232136452" + "\n" + "Address : 123455"
neworder_6 = "Customer name is: Jessy Tom John" + "\n" + "Order_id: 56136146" + "\n" + "Address : 457865"


print(neworder_1)
# print(neworder_2)
# print(neworder_3)
# print(neworder_4)
# print(neworder_5)
# print(neworder_6)
