import os
# from datetime import datetime
# # mod_time = os.stat("marina_practices.py").st_mtime
# # print(datetime.fromtimestamp(mod_time))
# # os.getcwd()
# # os.listdir()
# # print(os.listdir())
# # os.chdir()
# os.rename("problem_solve.py", "some_practices.py")
# print(os.listdir())


# print(os.getcwd())
# print(os.listdir())

# os.chdir("../..")
# print(os.getcwd(), "after")
# print(os.listdir())

# print(os.listdir("../.."))

# print("creating a dir")
# name = input("tell the name of the folder: ")
# os.mkdir(f"{os.getcwd()}/{name}")
# os.mkdir(f"{os.getcwd()}/{name}/test1")
# os.makedirs(f"{os.getcwd()}/{name}/test1")
# os.rmdir("test_2/test1")
#
# for path in os.listdir():
#     print(path)
#     if path == "marina1":
#         os.chdir(path)  # relative path
#         os.chdir(f"{os.getcwd()}/{path}")  # absolute
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


def append_username_in_file(path, username):
    if not os.path.exists(path):
        with open(path, "w"):
            pass

    with open(path) as f:
        data = f.read()

    with open(path, "a") as f:
        if not data:
            f.write("1 {}\n".format(username))
        else:
            rows = data.split("\n")
            row = rows[-2]
            number = int(row.split()[0]) + 1
            f.write("{} {}\n".format(number, username))


append_username_in_file("welcome_username.txt", "John")
append_username_in_file("welcome_username.txt", "Dohn")
append_username_in_file("welcome_username.txt", "Dohn")
append_username_in_file("welcome_username.txt", "Dohn")
append_username_in_file("welcome_username.txt", "Dohn")
append_username_in_file("welcome_username.txt", "Dohn")
append_username_in_file("welcome_username.txt", "Dohn")
