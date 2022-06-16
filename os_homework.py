import os

# print(os.getcwd())
# print(os.listdir())


# fp = open("file.txt", "w")
# fp.write("hello python")
# fp.close()


# name = input("tell the name of the folder: ")
# os.mkdir(f"{os.getcwd()}/{name}")
# os.mkdir(f"{os.getcwd()}/{name}/Dir2")
# os.mkdir(f"{os.getcwd()}/{name}/Dir3")
# os.makedirs("/Users/PC/Desktop/git_files/python_classes/dir1/Dir3/Dir4")


# ques = input("Do you want to delete all the dirs? y / n ")
# if ques == "y":
# if os.path.exists("file.txt"):
#     os.remove("file.txt")
#
# else:
#     print("The file does not exist")

os.chdir("/Users/PC/Desktop/git_files/python_classes/dir1")
while True:
    print(os.getcwd())
    path_list = os.listdir()
    print(path_list)

    try:
        os.rmdir(path_list[0])
    except OSError:
        os.chdir(path_list[0])
    else:
        break