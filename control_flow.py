# num = -45
#
# if num > 50:
#     print("Positive")
# elif num > 25:
#     print("Greater than 25")
# else:
#     print("Negative")
# def pass_fail(score):
#     return "pass" if score >= 50 else "fail"
#     # js
#     # return score >= 50 ? "pass" : "fail"
#
# print(pass_fail(49))
# students = ["john", "ivy", "kevin"]
#
# for student in students:
#     print(student)
# lang = "Python"
#
# for char in lang:
#     print(char)
# languages = ["Python", "JavaScript", "Typescript", "C++"]
#
# print("LANGUAGES THAT I KNOW")
#
# for lang in languages:
#     if lang == "JavaScript":
#         break
#     print(lang)
# attributes = ['Electric', 'Fast']
# cars = ['Tesla', 'Porsche', 'Mercedes']
#
# for car in cars:
#     for attribute in attributes:
#         print(car, attribute)
# number = 1
#
# while number <= 10:
#     print(number)
#     number += 1

# n = 10
#
# if n > 10:
#     pass
#
#
# print('Hello')
# from random import choice, shuffle
# shuffle(students)
#
# print(students)
# import math
# def calculate_area(radius):
#     return round(math.pi * math.pow(radius, 2), 2)
#
# print(calculate_area(5))
# student_list_1 = ["kevin", "mark", 'charity', "barrack"]
# student_list_2 = ["Fonte", "Nickson"]
# # print(students[:])
# # students.append("Ivy")
# # students.insert(0, "Joseph")
# # print(students)
# student_list_1.extend(student_list_2)
# # print(student_list_1)
# print(len(student_list_1))

numbers = [1, 200, 9, 4, 50]

# def find_largest(numbers):
#     max_number = 0
#     for num in numbers:
#         if num > max_number:
#             max_number = num
#     return max_number
def find_largest(numbers):
    length = len(numbers) -1
    return numbers.sort()

print(find_largest(numbers))

