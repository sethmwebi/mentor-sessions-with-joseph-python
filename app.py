# def modify_tuple(tupl, elem):
#     tupl = list(tupl)
#     tupl.append(elem)
#     return tuple(tupl)

# print(modify_tuple((1, 2, 3), 4))
# def myName(name):
#     return name 
#
# print(myName("Joe"))
# def full_name(first_name, last_name):
#     return f'{first_name} {last_name}'
#
# print(full_name("Barron", "Trump"))

# def implement_signup():
#    ...
# def divide(num1, num2=1):
#     return num1 / num2
#
# print(divide(5))
# def add_all(*args):
#     return sum(args)
#
# print(add_all(1,2,3,4,5))
# def greet(**kwargs):
#     for key, value in kwargs.items():
#         print(f'{key}: {value}')
#
# greet(name="Ivy", greet ="hi", president="Mr Emmanuel", celebrity="Kanye West")
# def add_numbers( a,  b = 5):
#     sum = a + b
#     print('Sum:', sum)
#
# add_numbers(6)
# def display_info(first_name, last_name):
#     return f'Hey my name is {first_name} {last_name}'
#
# print(display_info(last_name="Musk", first_name="Elon"))

# students = 23
#
# def get_num_of_students():
#     return students
#
# print(get_num_of_students())
# def outer():
#     message = 'local'
#
#     def inner():
#         nonlocal message
#
#         message = "nonlocal"
#         print("inner:", message)
#
#     inner()
#
#     print("outer:", message)
#
# outer()
# def factorial(x):
#     if x == 1:
#         return 1
#     else:
#         return (x * factorial(x - 1))
#
# print(factorial(5))
# from example import subtract
#
# print(subtract(6,7))
# import math
#
# print(math.gcd(12,18))
# from example import subtract as difference
#
# print(difference(10,5))
# import example
#
# # print(dir(example))
# print(example.__name__)
# from game.image import app
#
# app.image()
# print(__name__)
import helloworld
