# class Hotel(object):
#     LUX = "LUX"
#     STANDARD = "standard"
#
#     def __init__(self, name, room_amount_standard, standard_price, room_amount_lux, lux_price):
#         self.name = name
#         self.lux_price = lux_price
#         self.standard_price = standard_price
#         self.standard_rooms = self.construct_rooms(room_amount_standard)
#         self.lux_rooms = self.construct_rooms(room_amount_lux)
#         self.discount = None
#
#     @staticmethod
#     def construct_rooms(self, room_amount):
#         dict_ = {}
#         for room_number in range(room_amount + 1):
#             dict_[f"room_{room_number}"] = "Free"
#
#         return dict_
#
#     @classmethod
#     def shoe_room_types(cls):
#         return cls.LUX, cls.STANDARD
#  @staticmethod

# def shoe_room_types_static():
#     return Hotel.LUX, Hotel.STANDARD

#     def check_available(self, room_num, room_type):
#         if room_type == self.LUX:
#             room = self.lux_rooms.get(room_num)
#         elif room_type == "standard":
#             room = self.standard_rooms.get(room_num)
#         else:
#             raise ValueError("wrong key")
#
#         if not room:
#             raise ValueError("wrong key")
#         if room == "Free":
#             return True
#
#         return False
#
#     def book_room(self, room_num, room_type):
#         if room_type == self.LUX:
#             rooms = self.lux_rooms
#         elif room_type == self.STANDARD:
#             rooms = self.standard_rooms
#         else:
#             raise ValueError("wrong type")
#
#         if self.check_available(room_num, room_type):
#             rooms[room_num] = "Booked"
#             return True
#
#         return False
#
#     def calculate_price(self, room_type, amount=1):
#         room_price = self.lux_price if room_type == "lux" else self.standard_price
#         total_price = (room_price * amount)
#         if self.discount:
#             return total_price * (100 - self.discount) / 100
#
#         return total_price
#
#     def present(self):
#         return f"{self.name} our rooms \n {self.LUX} {self.lux_rooms}" \
#                f"{self.STANDARD} {self.standard_rooms}"
#
#
# hotel_1 = Hotel("Nairy", 5, 10, 25000, 15000)
# print(hotel_1.present())
# print(hotel_1.book_room("room_1", "lux"))
# print(hotel_1.book_room("room_1", "lux"))
#
# hotel_1.discount = 30
#
# print(hotel_1.calculate_price("lux", 4))
# new_dict = Hotel.construct_rooms(3)
# print(new_dict)

# Hotel.calculate_price("lux", 4)

# class Triangle(object):
#     created_triangles = 0
#
#     def __new__(cls, *args, **kwargs):
#         print("New object is created")  # self = super().__new__(cls)
#         self = super().__new__(cls)   # cls.created_triangles += 1
#         print(type(self))              # return self
#         return self
#
#     def __init__(self, *args):
#
#         self.a, self.b, self.c = args
#
#     def to_sorted_tuple(self):
#         return sorted((self.a, self.b, self.c))
#
#     def __gt__(self, other):
#         if not isinstance(other, Triangle):
#             raise TypeError(f"Not supported type {type(other)}")
#
#         first = self.to_sorted_tuple()
#         second = other.to_sorted_tuple()
#         is_greater = True
#         for i in range(3):
#             if first[i] <= second[i]:
#                 is_greater = False
#                 break
#         # return is_greater
#
#         return first[0] > second[0] and\
#                first[1] > second[1] and\
#                  first[2] > second[2]
#
#     def __eq__(self, other):
#         if not isinstance(other, Triangle):
#             raise TypeError(f"Not supported type {type(other)}")
#
#         return self.to_sorted_tuple() == other.to_sorted_tuple()
#
#     def __ne__(self, other):
#         return not self.__eq__(other)
#
#     def __del__(self):
#         # print(f"")
#         Triangle.created_triangles -= 1
#
#     # def perimeter(self):
#     #     return self.a + self.b + self.c


# triangle_1 = Triangle(1, 2, 3)
# # del triangle_1
# print("triangle_1 is deleted")
# triangle_2 = Triangle(4, 5, 6)
# triangle_3 = Triangle(4, 5, 6)
# print("I'm still here")
#
# if triangle_2 > triangle_1:
#     print(triangle_2, "is greater")

# print(triangle_3 == triangle_2)
# print(triangle_1 != triangle_2)
#
# print("Triangle count {}".format(Triangle.created_triangles))
# triangle_3 = 5


# class SingleToneClass(object):
#     instance = None
#     created_triangles = 0
#
#     def __new__(cls, *args, **kwargs):
#         if not cls.instance:
#             cls.instance = super().__new__(cls)
#
#            return cls.instance
#
#     def __init__(self, *args):
#
#         self.a, self.b, self.c = args
#
#     def to_sorted_tuple(self):
#         return self.to_sorted_tuple() == other.to_sorted_tuple()

import os

# print(os.getcwd())
# print(os.listdir())
#
# os.chdir("../..")
# print(os.getcwd(), "after")
# print(os.listdir())

# print(os.listdir("../.."))
#
# print("creating a dir")
# name = input("tell the name of the folder: ")
# os.mkdir(f"{os.getcwd()}/{name}")
# os.mkdir(f"{os.getcwd()}/{name}/test1")
# os.makedirs(f"{os.getcwd()}/{name}/test1")
# os.rmdir("test_2/test1")
#
# for path in os.listdir():
#     print(path)
#     if path == "test_2":
#         os.chdir(path)  # relative path
#         # os.chdir(f"{os.getcwd()}/{path}") absolute
#         for item in os.listdir(os.getcwd()):
#             if item.endswith(".txt"):
#                 os.remove(item)

# os.makedirs("/Users/tigran/Desktop/save/python_classes/dir1/test4/test2/test3")
# while True:
#     print(os.getcwd())
#     path_list = os.listdir()
#     print(path_list)
#
#     try:
#         os.rmdir(path_list[0])
#     except OSError:
#         os.chdir(path_list[0])
#     else:
#         break

# os.rename("test_1/text.txt", "test_1/text_2.txt")
# for path in os.listdir("test_1"):
#     prefix = "test_1"
#     path = f'{prefix}/{path}'
#     print(os.path.isabs(f'{os.getcwd()}/{path}'))
#     if os.path.isdir(path):
#         try:
#             os.rmdir(path)
#         except OSError:
#             print("Directory not empty")

# for path in os.listdir("test_1"):
#     prefix = "test_1"
#     # path = f'{prefix}/{path}'
#     path = os.path.join(os.getcwd(), prefix, path)
#     print(path, os.path.exists(path))

# file_path = os.path.join(os.getcwd(), "test_1", "text_1.txt")
# print(file_path)

# fd = open(file_path, "r")
# data = fd.read()
# fd.close()
# print(data)

# with open(file_path, "w") as file:
#     text = input("tell smth  ")
#     file.write(text)

# os.chdir("/Users/tigran/Desktop/save/python_classes/dir4")

# list_elements = os.listdir()
#
# for element in list_elements:
#     if os.path.isfile(element):
#         os.remove(element)
#     elif os.path.isdir(element):
#         os.rmdir(element)

# print(os.path.isabs("/Users/tigran/Desktop/save/python_classes/dir4"))
# print(os.path.isabs("dir4"))

# a = "dir4"
# b = "dir4/../dir4"
#
# # print(os.listdir(a))
# # print(os.listdir(b))
# os.chdir("/Users/tigran/Desktop/save/python_classes/dir4")
# #
# new_path = os.getcwd() + "/.." + "/databases_1"
#
# db_path = os.path.join(os.getcwd(), "..", "databases_1")
# print(os.path.exists(db_path))
# print(os.listdir(new_path))
# print(new_path)
# print(os.path.normpath(new_path))

file_path = os.path.join(os.getcwd(), "new_text_file.txt")

# file_obj = open(file_path, "w")  # for writing
# file_obj.write("Hello from python")
# file_obj.close()
#
# file_obj = open(file_path, "a")  # for appending
# file_obj.write("Hello from python\n")
# file_obj.close()

# file_obj = open(file_path, "r")  # for reading the same as open(file_path)
# data = file_obj.read()
# file_obj.close()
#
# print(data)
# print(data.split("\n"))
# rows = data.split("\n")
# rows.pop(-1)
# print(rows)
#
# # frameworks = []
# for row in rows:
#     frameworks.append(row.split()[-1])
#
# print(frameworks)
# file_path = "usernames.txt"
# with open(file_path, "r") as file_obj:
#     data = file_obj.read()
#
#
# class A:
#     def __init__(self, name):
#         self.name = name
#
#     def __enter__(self):
#         print("hello inside context manager")
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("finished exiting")

#
# a_obj = A("Context")
#
# with a_obj:
#     print("here I am")
#
# print("bye")


# def append_username_in_file(path, username):
#     if not os.path.exists(path):
#         with open(path, "w"):
#             pass
#
#     with open(path) as f:
#         data = f.read()
#
#     with open(path, "a") as f:
#         if not data:
#             f.write("1 {}\n".format(username))
#         else:
#             rows = data.split("\n")
#             row = rows[-2]
#             number = int(row.split()[0]) + 1
#             f.write("{} {}\n".format(number, username))
#
#
# append_username_in_file("welcome_username.txt", "John")
# append_username_in_file("welcome_username.txt", "Dohn")
# append_username_in_file("welcome_username.txt", "Dohn")
# append_username_in_file("welcome_username.txt", "Dohn")
# append_username_in_file("welcome_username.txt", "Dohn")
# append_username_in_file("welcome_username.txt", "Dohn")
# append_username_in_file("welcome_username.txt", "Dohn")

