# sample_str = '''string
# sample_str = "string value"
# sample_str = 'string value'
# sample_str = """string
# value"""
# value'''
# a = 1 + 2 + 3
# print(sample_str, a)
# sample_str = "string value"
# comp_number = 1 + 2j
# float_number = 5.5
# number = 8
# sample_bool = True
# sample_bool_2 = False
# # print(type(sample_str))
# # type_of_sample_string = type(sample_str)
# # print(type_of_sample_string)
# # print(type(float_number))
# # print(type(sample_bool))
# # print(type(comp_number))

# print(type("5.5"))
# result = sample_str + " " +str(float_number)
# # print(result)
# print(int(number + float_number))
# value = "6"
# print(int(value) + 8)
# value = -6
# zero = 0
# print(bool(value), bool(zero))
# print("*" * 0)
# print("*" * False)
# print("*" * True)
# num_1 = 2
# num_2 = 4

# print(num_1 ** num_2)
# print(10 / 20)
# print(10 % 20)
# print(10 // 20)
# print(complex("2+3j"))
# num_1 = num_1 + num_2
# # or
# num_1 += num_2

# num_1 = num_1 - num_2
# # or
# num_1 -= num_2

# num_1 -= num_2 + 6 + 8

# num_1 = num_1 // num_2
# # or
# num_1 //= num_2

# print(num_1)

# number_3 = 5
# is_even_reminder = number_3 % 2  # False
# print(is_even)
# print("It is even" * bool(is_even_reminder - 1), end="")
# print("It is odd" * bool(is_even_reminder), end="")
## or
# print("It is even" * bool(is_even_reminder - 1), "It is odd" * bool(is_even_reminder), sep="")

# c = float(input("Tell the temperature in celsius\n"))
# f = c * 1.8 + 32
# print("in fahrenheit it will be ", f)
# radius = float(input("tell the radius and see the area\n"))
# area = radius ** 2 * 3.14
# print("the area of circle with given radius is:", area)
# name = input("tell your name: ")
# surname = input("tell your surname: ")
# print(surname, name)
# name = "John"
# name = "Jack"
# a = print(5)  # None
# print(a)
# option 1
# import variables
# import variables as vbs
# print("current date is: ", vbs.year, vbs.month, vbs.day)
# print("current date is: ", variables.year, variables.month, variables.day)
# option 2
# from variables import year, day, month
# option 3
# from variables import *
# print("current date is: ", year, month, day)
# import datetime
# current_date = datetime.datetime.now()
# print(current_date)
# print(current_date.year)
# print(current_date.day)
# print(current_date.month)
# print(current_date.date())
# print(current_date.hour)
# print(current_date.minute)
# print(current_date.second)
# print(current_date.microsecond)
# print(current_date.tzinfo)
# print(current_date.time())
# current_date_2 = datetime.datetime.now()
# print(current_date, current_date_2)
# current_date = datetime.datetime.now()
# age = int(input("Tell your age and see in which year you will be 100 years old\n"))
# diff_of_100 = 100 - age
# date_of_100_years_old = current_date.year + diff_of_100
# print("you'll be 100 years old in", date_of_100_years_old)

# my_number = 5
# user_number = int(input("Tell me a number: "))
# print("they are equal", my_number == user_number)
# print("they are not equal", my_number != user_number)
# print("It is or 5 or greater than 5", user_number >= my_number)
# print("It is or 5 or greater than 5", user_number > my_number or user_number == my_number)
# # 13
# print("It is greater than 5 and it is devidable by 5", user_number > my_number and not (user_number % my_number))

# name = "Jo hn"
# print("o" in name)
# print("John" in name)
# print("John " in name)
# number = int(input("tell a number\n"))
# if number > 5:
#     print("it is greater than five")
#     if number % 5:
#         pass
#     else:
#         print("and it is devidable by 5")
# elif number == 5:
#     print("it is 5")
# elif number == 0:
#     print("it is 0")
# else:
#     print("it is lower than five")
# print("bye")
# a = 28
# if a > 7:
#     print(">7")
# if a > 20:
#     print(">20")
# else:
#     pass

# my_text = "this is a string"
# print("length of the string is: ", len(my_text))
# print(my_text[0])
# print(my_text[-16])
# # print(my_text[16])  # invalid
# # print(my_text[start:don't_take_this])
# print(my_text[:])
# print(my_text[1:])
# print(my_text[-3:])
# print(my_text[-3:-1])
# print(my_text[-100:-3])
# print(my_text[0:1000])
# # my_text[start:don't_take_this:step]
# print(my_text[0:1000:2])
# print(my_text[1:1000:2])
# print(my_text[0:1000:-1])
# print(my_text[::-1])
# print(my_text[::-2])
# print(my_text[::15])
# print(my_text[::15])
# # get 'is' from my_text reverced
# print(my_text[6:4:-1]) #  >>> si
# text = "Armenia"

# print(text.index("Arm"))
# print(text.index("menia"))
# word = "approve"
# print(word.index("p"))
# print(word.index("p"))
# text = "Armenia"
# print(text.find("Arm"))
# print(text.find("arm"))
# fruit = "apple"
# print(fruit.endswith("e"))
# print(fruit.endswith("l"))
# print(fruit.endswith(""))
# sentence = "Hello python world"
# new_one = sentence.replace("python", "django")
# print("old sentence: ", sentence, "\nnew sentence", new_one)
# sentence = "Hello hello python world"
# new_one = sentence.replace("ello", "i")
# # print("old sentence: ", sentence, "\nnew sentence", new_one)
# # final_text = "old sentence: " + str(sentence) + "\nnew sentence" + str(new_one)
# # print(final_text)
# final_text = "old sentence: {}\nnew sentence {}".format(sentence, new_one)
# print(final_text)
# # final_text = "old sentence: {}\nnew sentence {}"
# # # final_text_formated = final_text.format(sentence, new_one)
# user_name = "John"
# age = 28
# part = 0.25
# congrats_text = "Dear {} happy {}-th anniversary you have already lived about {} part of your life"
# print(congrats_text.format(user_name, age, part))
# print(congrats_text.format("Jack", 38, 0.2))
# congrats_text = "Dear {name} happy {age}-th anniversary you have already lived about {part} part of your life"
# print(congrats_text.format(age=age, name=user_name, part=part))
# congrats_text = f"Dear {user_name} happy {age}-th anniversary you have already lived about {part} part of your life"
# print(congrats_text)
# a = "hello %s" %user_name
# print(a)
# range_num = range(1, 5, 1)
# range_num = range(0, 5, 1)
# range_num = range(5)
# print(range_num)
# print(chr(65), chr(97))
# print(ord("A"), ord("a"))
# year = int(input("enter year to check for leap year "))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("{1} is a leap year {0}".format(year, year + 1))
#         else:
#             print("{0} is not leap year".format(year))
#     else:
#         print("{0} is a leap year".format(year))
# else:
#     print("{0} is not leap year".format(year))
# if year % 400 == 0:
#     print("leap")
# elif year % 100 == 0:
#     print("not leap")
# elif year % 4 == 0:
#     print("leap")
# else:
#     print("not leap")
# if year % 400 == 0 or (year % 4 and not year % 100) or new_year % 4:
#     print("leap")
# else:
#     print("not leap")
# a = 6
# if a > 5 and b < 10:
#     pass

from datetime import datetime as dt
# sentence = "bla bla bla not bla poor bla  not bla poor"
# # not_index = sentence.find("not")
# # poor_index = sentence.find("poor")
# # if not_index >= 0 and poor_index > not_index:
# # 	sentence = sentence.replace(sentence[not_index: poor_index + 4], "good")
# # print(sentence)
# new_sentence = sentence[0] + sentence[1:].replace(sentence[0], "$")
# print(new_sentence)
# word = "Hello Pyhton"
# for i in word:
# 	print(i)
# i = word[0]
# print(i)
# i = word[1]
# print(i)
# i = word[2]
# print(i)
# for i in range(5):
# 	print(i)
# name = input("tell your name:\n")
# amount_of_prints = int(input("How many time do you want to print?:\n"))
# sentence = f"hello {name}"
# for _ in range(amount_of_prints):
# 	print(sentence)
# i = "hello world"
# for i in range(6):
# 	if i % 2 == 0:
# 		print("even")
# 	else:
# 		print("odd")
# print(i)
# print("{} x 5 = {}".format(1, 1*5))
# print("{} x 5 = {}".format(2, 2*5))
# print("{} x 5 = {}".format(3, 3*5))
# ## ...
# print("{} x 5 = {}".format(10, 10*5))
## or
# for num in range(11):
# 	print("{} x 5 = {}".format(num, num * 5))
# user_num = int(input("tell the number: "))
# for i in range(1, user_num):
# 	if i % 15 == 0:
# 		print("FizzBuzz")
# 	elif i % 3 == 0:
# 		print("Fizz")
# 	elif i % 5 == 0:
# 		print("Buzz")
# 	else:
# 		print(i)
#              str(2022)
# year_str = str(dt.now().year)
# sum_of_digits = 0
# for digit in year_str:
# 	sum_of_digits += int(digit)
# print(sum_of_digits)
# text = "a0b0"
# count_num = 0
# if text[0].isdigit():
# 	count_num +=1
# if text[1].isdigit():
# 	count_num +=1
# if text[2].isdigit():
# 	count_num +=1
# if text[3].isdigit():
# 	count_num +=1
# print(count_num)
# print("5b".isdigit())
# print("b".isalpha())
# text = "a0b0909809"
# count_num = 0
# count_letters = 0
# for dig in text:
# 	if dig.isdigit():
# 		count_num += 1
# 	elif dig.isalpha():
# 		count_letters += 1
# print(count_num)
# print(count_letters)
# text = "a0b0909809"
# count_num = 0
# count_letters = 0
# for dig in text:
# 	if dig.isdigit():
# 		if int(dig) % 2 == 0:
# 			count_num += 1
# 	elif dig.isalpha():
# 		count_letters += 1
# print(count_num)
# print(count_letters)
# text = "a0b0909809"
# sum_num = 0
# count_letters = 0
# for j in text:
# 	if j.isdigit():
# 		sum_num += int(j)
# print(sum_num)
# text = "a0b0"
# count_num = 0
# for i in text:
# 	if i.isdigit():
# 		count_num += 1
# 	else:
# 		print("couldn't find")
# 		continue
# 	print("I've found one more number")
# text = "0350asdas87678"
# count_num = 0
# for i in text:
# 	if not i.isdigit():
# 		continue
# 	num = int(i)
# 	if num % 2 == 0:
# 		count_num += 1
# text = "0350asdas87678"
# count_num = 0
# for i in text:
# 	print(f"now analyzing {i}")
# 	if i.isdigit():
# 		count_num += 1
# 	else:
# 		print("couldn't find")
# 		break
# 	print("I've found one more number")
# for i in range(5):
# 	continue
# else:
# 	print("ran without errors")
# sum_ = 0
# for i in range(1, 21):
# 	if i == 3 or i == 13:
# 		continue
# 	sum_ += i
# sum_ = 0
# for i in range(1, 21):
# 	if not i % 2:
# 		continue
# 	sum_ += i
# sum_ = 0
# for i in range(1, 21):
# 	if sum_ >= 15:
# 		break
# 	sum_ += i

# text = "abcd"
# # print(text[::2])
# # for i in range(0, len(text), 2):
# # 	print(text[i])
# #              range(4)
# for i in range(0, len(text), 2):
# 	if i % 2 == 0:
# 		print(text[i])
# #           True/False
# i = input()
# if i.isdigit():
# 	i = int(i)
# print(i % 2)
# #
# # import sys
# # i = input("digit: ")
# # if i.isdigit():
# # 	i = int(i)
# # else:
# # 	print("not digit")
# # 	sys.exit()
# # print(i % 2)
# # for j in range(i):
# 	# user_choice = input("continue? if yes type yes ")
# 	# if user_choice != "yes":
# 	# 	sys.exit()
# # print("good bye")
# numbers = range(1, 11)
# even = 0
# odd = 0
# for i in numbers:
#     if i % 2 == 0:
#     	print(even)
#         even += 1
#     else:
#         odd += 1
# print("Even numbers {} and odd numbers {}".format(even, odd))
# print(f"Even numbers {even} and odd numbers {odd}")
# num = int(input("give num and see the divisors of it: "))
# for i in range(1, int(num / 2) + 1):
# 	if num % i == 0:
# 		print(i)
# print("and don't forget about {}".format(num))
# for i in range(1, int(num ** 0.5) + 1):
# 	if num % i == 0:
# 		print(i, num / i)
# print("and don't forget about {}".format(num))
# number = int(input("tell the number: "))
# number = 1
# for i in range(1, 11):
# 	print("{} x {} = {}".format(number, i, number * i))
# number = 2
# for i in range(1, 11):
# 	print("{} x {} = {}".format(number, i, number * i))
# number = 3
# for i in range(1, 11):
# 	print("{} x {} = {}".format(number, i, number * i))
# or
# for number in range(1, 11):
# 	print("\nhere comes multiplication table of {}\n".format(number))
# 	for i in range(1, 11):
# 		print("{} x {} = {}".format(number, i, number * i))
# for i in range(1, 11):
# 	print(i * "*")
# print()
# for i in range(1, 11):
# 	for j in range(i):
# 		print("*", end="")
# 	else:
# 		print()
# 	# print("---------")
# while True:
# 	user_password = input("tell password: ")
# 	if len(user_password) >= 8:
# 		break
# 	else:
# 		print("too short")
# user_password = input("tell password: ")
# while len(user_password) < 8:
# 	user_password = input("too, short\ntell password again: ")
# print(f"{user_password} is successfully set")
# user_password = input("tell password: ")
# while len(user_password) < 8:
# 	user_password = input("too, short\ntell password again: ")
# print(f"{user_password} is successfully set")
# with for
# text = "abcd"
# for letter in text:
# 	print(letter)
# # with while loop
# idx = 0
# while idx < len(text):
# 	print(text[idx])
# 	idx += 1
# check = True
# while check:
# 	user_pass = input("tell password: ")
# 	if len(user_pass) < 8:
# 		continue
# 	pass_check_num = False
# 	pass_check_symbol = False
# 	for i in user_pass:
# 		if i.isdigit():
# 			pass_check_num = True
# 			continue
# 		if not i.isdigit() and not i.isalpha():
# 			pass_check_symbol = True
# 	if  pass_check_symbol and pass_check_num:
# 		check = False
# print("password is set")
# check = True
# while check:
# 	user_pass = input("tell password: ")
# 	if len(user_pass) < 8:
# 		continue
# 	pass_check_num = False
# 	pass_check_symbol = False
# 	for i in user_pass:
# 		if i.isdigit():
# 			pass_check_num = True
# 			continue
# 		elif not i.isalpha():
# 			pass_check_symbol = True
# 	if  pass_check_symbol and pass_check_num:
# 		check = False
# print("password is set")

# height = input("enter the height ")
# while not height.isdigit():
# 	height = input("enter the height ")
# else:
# 	height = int(height)
# for i in range(1, height * 2):
# 	if i <= height:
# 		print("*" * i)
# 	else:
# 		print("*" * (height * 2 - i))
# 0, 1, 1, 2, 3, 5, 8, 13, 21
# x = 0
# y = 1
# c = x + y # 1
# x = y
# y = c
# c = x + y
# x = y
# y = c
# c = x + y
# x = 0
# y = 1
# c = 0
# while c <= 50:
# 	c = x + y
# 	x = y
# 	y = c
# x, y = 0, 1
# while y <= 50:
# 	print(y)
# 	x, y = y, x + y
# import random
# comp_win_amount = 0
# user_win_amount = 0
# draw_amount = 0
# check = True
# while check:
# 	user_choice = int(input("rock: 1 or paper: 2 or scissors: 3\n"))
# 	comp_choice = random.randint(1, 3)
# 	if user_choice == comp_choice:
# 		print("Draw")
# 		draw_amount += 1
# 	elif user_choice == 1 and comp_choice == 3 or \
# 		user_choice == 2 and comp_choice == 1 or \
# 		user_choice == 3 and comp_choice == 2:
# 		print("User Wins")
# 		user_win_amount += 1
# 	else:
# 		print("Computer Wins")
# 		comp_win_amount += 1
# 	user_answer = input("Play again? Type y for yes\n")
# 	if user_answer.lower() != "y":
# 		check = False
# else:
# 	amount_of_play = comp_win_amount + user_win_amount + draw_amount
# 	print("You have played {} times, you won {} times, computer won {} times and draw amount is {}".format(amount_of_play, user_win_amount, comp_win_amount, draw_amount))
# def my_function():
# 	print("hello function")
# 	print("hello function")
# 	print("hello function")
# # print(my_function)
# my_function()
# def say_happy(name):
# 	pass
# print(print()) #  returns None
# print(input()) #  returns the inputted value
# def say_happy(name):
# 	text = "Happy birthday dear {}\nwish you all the best".format(name)
# 	print("finished")
# 	return text
# text_1 = say_happy("Jack")
# name_1= "Jane"
# text_2 = say_happy(name_2)
# print(text_1)
# print(text_2)
# text = "new_one"
# def say_happy(name):
# 	global text
# 	text = "Happy birthday dear {}\nwish you all the best".format(name)
# 	# print(text)
# 	return text
# print(text_1)
# print(text_2)
# text_form = say_happy("Jane")
# if "Jane" in text_form:
# 	new_text = text_form.replace("Jane", "John")
# print(text)
# def say_happy(name="Someone"):
# 	text = "Happy birthday dear {}\nwish you all the best".format(name)
# 	return text
# text_form = say_happy("Jane")
# text_form_2 = say_happy()
# print(text_form)
# print(text_form_2)
# def is_even(num):
# 	#          6
# 	return int(num) % 2 == 0
# print(is_even(5))
# print(is_even(6))
# def sum_count_of_even_digits(word):
# 	count_ = 0
# 			# wdkhakbn6735723
# 	for i in word:
# 		#              first value 6
# 		if i.isdigit() and is_even(i):
# 			count_ += 1
# 	return count_
# print(sum_count_of_even_digits("wdkhakbn6735723"))
# def get_factorial(num):
# 	if num == 0 or num == 1:
# 		return 1
# 	factorial = 1
# 	for i in range(num):
# 		factorial *= i
# 	return factorial
# def validate_triangle(a, b, c):
# 	valid = False
# 	if a + b >= c and a + c >= b and c + b >= a:
# 		valid = True
# 	return valid
# def perimeter(a, b, c):
# 	if validate_triangle(a, b, c):
# 		return a + b + c
# 	else:
# 		raise ValueError("Not a valid triangle")
# print(perimeter(3, 5, 4))
# print(perimeter(3, 5, 15))

# from typing import Union
# def perimeter(a: Union[float, int], b: int, c: float) -> float:
#   """
#   Returns the perimeter of the triangle
#   Params:
#       a Union[float, int]: first side
#   return: the perimeter in type of float
#   """
#     return a + b + c
# # name: str = "Jack"
# print(perimeter.__doc__)
# help(perimeter)
# # print(perimeter.__annotations__)

# ____________________ TUPLE ______________________ #

# sample_tuple = (1, 20, 3, 4, True, "BMW")
# sample_tuple = 1, 20, 3, 4, True, "BMW", "BMW"
# one_element_tuple = ("one",)

# print(sample_tuple[-1][-1], "returns W from BMW")
# print(sample_tuple[-1].isalpha(), "checks if the last elemnt is alpha")
# # tuple(1) >>> will raise error
# print(tuple("bac"))
# print(id(sample_tuple))
# sample_tuple_changed = (2,) + sample_tuple[1:]
# sample_tuple = sample_tuple_changed
# print(id(sample_tuple))
# print(sample_tuple)
# sample_tuple = 1, 20, 3, 4, True, "BMW", "BMW", False
# # print(len(sample_tuple))
# # print(sample_tuple.index("BMW"))
# print(sample_tuple.count("BMW"))
# print(sample_tuple.count(1))
# print(sample_tuple.count(True))
# print(sample_tuple.count(0))
# del sample_tuple #  deletes tuple object
# sample_tuple #

# def sum_numbers_in_tuple(tuple_1: tuple) -> float:
#     type_of_numbers = (int, float)

# sum_ = 0.0
# for item in tuple_1:
#     if type(item) in type_of_numbers:  # if type(item) is int or type(item) is float:
#         sum_ += item
# return sum_
# sample_tuple = (1, 20, 3, 4, True, "BMW", "BMW", False, 1.5)
# sample_tuple_1 = (3, 4, True, "BMW", "BMW", False, 1.5)
# sample_tuple_2 = (3, 4, 5)
# result = sum_numbers_in_tuple(sample_tuple)
# print(result)
# def sum_numbers_in_multiple_tuples(*args):
#     total_sum = 0
#     for tup in args:
#         total_sum += sum_numbers_in_tuple(tup)
#     return total_sum
#     result = sum_numbers_in_multiple_tuples()
#     result = sum_numbers_in_multiple_tuples(sample_tuple)
#     result = sum_numbers_in_multiple_tuples(sample_tuple, sample_tuple_1)
#     result = sum_numbers_in_multiple_tuples(sample_tuple, sample_tuple_1, sample_tuple_2)
#     print(result)
    # args = (sample_tuple, sample_tuple_1, sample_tuple_2)
    # sum_numbers_in_multiple_tuples(*args)
    # tuple_1 = (1, 2, 3)
    # print(tuple_1, sep="---")
    # print(*tuple_1, sep="---") # print(1, 2, 3)
    # def sum_numbers_in_multiple_tuples(tupl_1, tuple_2, *args):
    #     total_sum = sum_numbers_in_tuple(tupl_1) + sum_numbers_in_tuple(tuple_2)

    #     for tup in args:
    #         total_sum += sum_numbers_in_tuple(tup)
    #     return total_sum

# def sum_letters(tuple_1: tuple) -> int:
#     count_ = 0
#     for item in tuple_1:
#         if type(item) is str:
#             for let in item:
#                 if let.isalpha():
#                     count_ += 1
#     return count_
# # def compare_letters_count_for_tuples(tup_1, tup_2):
# #     return sum_letters(tup_1) == sum_letters(tup_2)
# def compare_letters_count_for_multiple_tuples(*args):
#     check = False
#     first_count = sum_letters(args[0])
#     for tuple_ in args[1:]:
#         if sum_letters(tuple_) != first_count:
#             return check
#     return True
# # t_1 = ("abc", 56, "j5k")
# # t_2 = ("gbd", 56, "jk")
# # print(compare_letters_count_for_tuples(t_1, t_2))
# # print(compare_letters_count_for_multiple_tuples(t_1, t_2))
# t_3 = ("abc", 56, "j5k")
# t_4 = ("gbd", 56, "jk")
# # print(compare_letters_count_for_tuples(t_3, t_4))
# # print(compare_letters_count_for_multiple_tuples(t_3, t_4))
# a = (1, 2)
# a += (3,)
# print(a)
# list_1 = list()
# list_2 = list(a)
# list_3 = []
# print(list_1, "before append", id(list_1))
# list_1.append(True)
# list_1.append([1, 2])
# list_1.append((5, False))
# print(list_1, "after append")
# list_1.insert(3, "text")
# print(list_1, "after insert", id(list_1))
# print("removing")
# list_1.remove("text")
# print(list_1, "after remove")
# # list_1.pop(0)
# return_value = list_1.pop(0)
# print(list_1, "after pop")
# del list_1[0]
# print(list_1, "after del")
# list_1.clear()
# print(list_1, "after clear")
# sample_list = [1, 2]
# copy_list = sample_list
# sample_list.append(5)
# print(copy_list)
# sample_list = [1, 2]
# copy_list = sample_list.copy()
# sample_list.append(5)
# print(copy_list, sample_list)
# print(id(copy_list), id(sample_list))
# sample_list = [500, 2, [500, 5]]
# copy_list = sample_list.copy()
# print(copy_list, sample_list)
# print(id(copy_list), id(sample_list))
# sample_list[2].append(7)
# print(copy_list, sample_list)
# print(id(copy_list), id(sample_list))
# # print(sample_list[0] is sample_list[2][0])
# # print(id(sample_list[0]), id(sample_list[2][0]))
# print(sample_list[2] is sample_list[2])
# from copy import deepcopy
# sample_list = [500, 2, [500, 5]]
# copy_list = deepcopy(sample_list)
# sample_list[2].append(7)
# print(copy_list, sample_list)
# print(id(copy_list), id(sample_list))
# sample_tuple = (1, 2, [4, 5])
# sample_tuple[2].append(6)
# print(sample_tuple)
# sample_list = [1, 2]
# sample_list_1 = [3, 4]
# sample_list.extend(sample_list_1)
# print(sample_list)
# sample_list = [1, 4, 2]
# a = sample_list
# sample_list_1 = [3, 4]
# print(id(sample_list))
# sample_list = sample_list + sample_list_1
# print(id(sample_list), sample_list, a)
# sample_list.sort(reverse=True)
# print(sample_list)
# print(sorted(sample_list))
# print(sample_list)
# def get_second_largest(l_1):
#     # return sorted(l_1)[-2]
#     l_2 = l_1.copy()
#     l_2.sort()
#     return l_2[-2]
#
# import random
# b = [1, 2, 3]
# c = [1, 4, 9, 6]
# a = []
# for i in b:
#     if i in c and i not in a:
#         a.append(i)
# c.sort()  # >>> None
# print(c)  # >>> [1, 4, 6, 9]
# c.sort(reverse=True)
# print(c)  # >>> [9, 6, 4, 1]
# print(sorted(c))  # >>> [1, 4, 6, 9]
# print(c)  # >>>> [1, 4, 9, 6]
# sample_list = [1, 4, 9, 6]
# for i in sample_list:
#     random_num = random.randint(0, 5)
#     try:
#         result = i / random_num
#     except:
#         result = "Random generated 0"
#     else:
#         print("0 wasn't generated")
#     finally:
#         print("finished")
#     print(result)
# case with finally
# random_num = random.randint(0, 5)
# print("asdasdas")
# try:
#     b = 5 / random_num
# finally:
#     print("turning off all the sensors")
# random_num = random.randint(0, 1)
# if random_num:
#     a = "hello"
# num = input("tell number greater than 5: ")
# try:
#     number = int(num)
#     if number > 5:
#         x = "number is greater than"
#     print(x)
# except ValueError:
#     print("You have provided wrong value {}".format(num))
# except NameError:
#     print("You have provided number less or equal than five {}".format(num))
# except Exception:
#     print("something strange happened")

# def flattern_list(list_1: list) -> list:
#     if type(list_1) is not list:
#         raise ValueError("You have provided not a list object")

# new_list = []
# for i in list_1:
#     if type(i) is int:
#         new_list.append(i)
#     else:
#         new_list.extend(i)
# return new_list
# sample_list = [1, [4, 9], 6]
# print(flatten_list(sample_list))
# def flatten_list_buggy():
#     print("perfect")
#     raise
#     print("perfect")
# flatten_list_buggy()
# list_of_lists = [
#     [1, [4, 9], 6],
#     [1, 5, 6],
#     (1, [4, 9], 6)
#     ]
# summary = []
# for list_ in list_of_lists:
#     try:
#         result = flatten_list(list_)
#     except ValueError as err:
#         print(err)
#         result = []
#     summary.extend(result)
# print(summary)

# dict_1 = {"key_1": "apple", "key_2": (1, 4), "key_3": [1, 12]}
# dict_1 = {
#     "key_1": "apple",
#     "key_2": (1, 4),
#     "key_3": [1, 12]
#     }
# dict_1 = dict(
#     key_1="apple",
#     key_2=(1, 4),
#     key_3=[1, 12]
#     )
# dict_2 = {}
# dict_2 = dict()
# print(dict_1)
# dict_1 = {
#     50: "apple",
#     "key_2": (1, 4),
#     (1, 2): [1, 12]
#     }
# print(dict_1[50])
# print(dict_1["key_2"])
# print(dict_1[(1, 2)])
# print(dict_1.get("key_2", False))
# print(dict_1.get("key_3", False))
# print(dict_1[(1, 2, 3)])
# dict_1 = {
#     "key_1": "apple",
#     "key_2": (1, 4),
#     "key_3": [1, 12],
#     "key_4": "orange"
#     }
# dict_1[50] = 60
# dict_1["key_3"] = 70
# print(dict_1)
# for i in dict_1:
#     print("the value of key {} is {}".format(i, dict_1[i]))
# print(dict_1.pop("key_1"))
# print(dict_1.popitem())
# dict_1.clear()
# print(dict_1)
# del dict_1["key_4"]
# print(dict_1)
# print(dict_1)
# print(dict_1.keys(), type(dict_1.keys()))
# print(dict_1.values(), type(dict_1.values()))
# print(dict_1.items(), type(dict_1.items()))
# dict_1 = {
#     "key_1": "apple",
#     "key_2": (1, 4),
#     "key_3": [1, 12],
#     "key_4": "orange"
# }
# dict_2 = {
#     "key_1": "banana",
#     "key_5": "tomato"
# }
# dict_1.update(dict_2)
# print(dict_1)
# dict_3 = {
#     "key_1": "apple",
#     "key_2": "apple",
#     "key_3": "apple",
#     "key_4": "apple"
#     }
# dict_3 = dict.fromkeys(('key_1', 'key_2', 'key_3', 'key_4'), "apple")
# print(dict_3)

# dict_3 = {
#     "key_1": "apple",
#     "key_2": "apple",
#     "key_3": "apple",
#     "key_4": "apple",
#     "key_1": "banana"
# }
#
# print(dict_3)
# set_1 = {1, 2, (1, 4), "abc", 3, 4, 1, "abc", 1}
# print(set_1)
# list_1 = [1, 1, 1, 5, 6]
# print(list(set(list_1)))

# list_1 = [1, 1, 1, [1, 4], 5, 6, [1, 4]]
# print(list(set(list_1)))
# list_1 = [1, 1, 1, (1, 4),  5, 6, (1, 4)]
# print(list(set(list_1)))
# dict_1 = {{1, 6, 5}: "new dict"} # error
# print(dict_1)
# set_1 = set()
# set_1.add(1)

# set_1 = {1, 3, 5}
# set_2 = {2, 3, 4}
# result = set_1. difference(set_2)
# print(result)

# def new_function(value):
#     a = 0
#     print(value)
#
#     if len(value) < 9:
#         for i in range(len(value)):
#             try:
#                 i = int(i)
#             except:
#                 i = 0
#
#             a += i
#         return a
#     else:
#         return 0
#
#
# final_value = new_function("09a7a6a9")
# print(final_value)
