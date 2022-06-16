import json
import os
import yaml

# print(os.getcwd())
# students = []
# while True:
#     input_ = input("name surname? ")
#     name = input_.split()[0]
#     surname = input_.split()[1]
#     dict_ = dict(
#         name=name,
#         surname=surname
#     )
#     students.append(dict_)
#     # print(students)
#     check = input("Enough? yes for exit: ")
#     if check == "yes":
#         break
# with open("new_file.json", "w") as json_file:
#     print("The json file is created")
#     json.dump(students, json_file, indent=4)


#  json file convert to text file

# json_obj = json.dumps(students)
# with open("text.txt", "w") as txt_file:
#     print(txt_file.write(json_obj))

# with open("new_.yaml", "w") as yaml_file:
#     print(yaml_file.write(json_obj))

#  Yaml file convert to json file


# doctors = []
# while True:
#     input_ = input("name surname? ")
#     name = input_.split()[0]
#     surname = input_.split()[1]
#     dict_ = dict(
#         name=name,
#         surname=surname
#     )
#     doctors.append(dict_)
#     # print(doctors)
#     check = input("Enough? yes for exit: ")
#     if check == "yes":
#         break
# with open("new_file.yaml", "w") as yaml_file:
#     print("The yaml file is created")
#     yaml.dump(doctors, yaml_file, indent=4)
#
#
# #  yaml file convert to text file
#
# yaml_obj = yaml.dumps(doctors)
# # with open("text.txt", "w") as txt_file:
# #     print(txt_file.write(yaml_obj))
#
# # yaml file convert to json file
# with open("new_.json", "w") as json_file:
#     print(json_file.write(yaml_obj))
