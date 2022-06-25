import json
import os
import time
import requests
import threading
import datetime


class Image:
    def __init__(self, name, url, path=None):
        self.name = name
        self.url = self.validate_url(url)
        self.default_path = path if path else os.getcwd()

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

    def download(self):
        response = self.send_request_safe(self.url)

        if response.status_code == 200:
            img_address = f"{self.default_path}/{self.name}"
            with open(img_address, "wb") as file:
                file.write(response.content)

        print("Downloaded")


class FromJson2Image:
    def __init__(self, json_file_path):
        self.json_file_path = self.validate_path(json_file_path)
        self.image_dict = self.read_from_json()
        self.image_list = self.create_images_from_dict()

    @staticmethod
    def validate_path(path):
        if not os.path.exists(path):
            raise ValueError("wrong path")
        return path

    def read_from_json(self):
        with open(self.json_file_path) as json_file:
            data = json.load(json_file)
        return data

    def create_images_from_dict(self):
        image_list = []
        for dict_ in self.image_dict:
            image_list.append(Image(name=dict_["img_name"], url=dict_["img_url"]))

        return image_list

    def download_all_images(self):
        for image in self.image_list:
            image.download()

    def download_with_td(self):
        thread_list = []

        def function_1():
            for image in self.image_list:
                time.sleep(0.1)
                image.download()
        t = threading.Thread(target=function_1)
        thread_list.append(t)
        t.start()

        for thread in thread_list:
            thread.join()


if __name__ == "__main__":
    json_to_image = FromJson2Image(json_file_path="img_links.json")
    json_to_image.download_with_td()
    # json_to_image.download_all_images()
starting_time = datetime.datetime.today()
b = (datetime.datetime.today() - starting_time).seconds
print(f"it took {b} seconds")




