import requests


# response = requests.get("https://www.uu.se/digitalAssets/805/c_805646-l_1-k_image.jpg")
#
# file = open("sample1_image.png", "wb")
# file.write(response.content)
# file.close()

# def download_image(url, name):
#
#     with open(f"{name}.jpeg", "wb") as photo:
#         try:
#             response = requests.get(url)
#         except Exception as err:
#             print(f"smth happened {err}")
#         if response.status_code == 200:
#             photo.write(response.content)
#             print(f"image {name} is downloaded")


# url = "https://www.uu.se/digitalAssets/805/c_805646-l_1-k_image.jpg"
# name = "new_pic1"
#
# print(download_image(url, name))


# url = "https://cdn.pixabay.com/photo/2020/05/12/17/04/wind-turbine-5163993_960_720.jpg"
#
# r = requests.get(url)
# with open("my_pic1.jpg", "wb") as f:
#     f.write(r.content)
