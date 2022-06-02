# HW1
# dic1 = {1: 10, 2: 20}
# dic2 = {3: 30, 4: 40}
# dic3 = {5: 50, 6: 60}
# dic4 = {6: 50, 7: 60}
# new_dic = {}
# for k in (dic1, dic2, dic3):
#     new_dic.update(k)
# print(new_dic)

# HW2
# n = int(input("enter a number"))
# d = dict()
# for x in range(1, n + 1):
#     d[x] = x * x
#
# print(d)



# HW3
def after_dropping(my_dict):
    d = list(my_dict)
    for key in d:
        if key is not None:
            my_dict.pop(key)
            print(my_dict)
            break
my_dict = {"c1": "Red", "c2": "Green", "c3": None}

after_dropping(my_dict)


# HW4
# set_1 = {"a", "b", "Red", "Green"}
# set_2 = {"b", "a", "Red", "Green"}
# set_3 = set_1.copy()
# print(set_1)

# HW5
# set_1 = {3, 10, 1, 4, 5, 9, 2}
# print("minimum value is :", min(set_1))
# print("maximum value is: ", max(set_1))

# HW6
# set_1 = {1, 2, 3, 4}
# set_2 = {4, 5, 6, 7}
# print(set_1)
# print(set_1.difference(set_2))
# print(set_2)
# print(set_2.difference(set_1))
