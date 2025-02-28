# class Student:
#     name = ""
#     age = 0
#
# student_1 = Student()
# student_1.name = "Maureen"
# student_1.age = 19
#
# student_2 = Student()
# student_2.name = "Kevin"
# student_2.age = 20 
#
# print(f'The best student in out class is {student_1.name} and she is {student_1.age} years old')
# print(f'{student_2.name} who is {student_2.age} years old is also another student in my class')
# class Rectangle:
#     width = 0
#     length = 0
#
#     def area(self):
#         return f'The area of the rectangle is {self.width * self.length}'
#
# rect1 = Rectangle()
# rect1.width = 2
# rect1.length = 5
# print(rect1.area())
# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade
#
#     def score(self):
#         return f'{self.name} who is {self.age} garnered an average grade of {self.grade} in the final exam'
#
#
# stud1 = Student("Ivy", 19, "A")
# stud2 = Student("Kevin", 20, "B")
# print(stud1.score())
# print(stud2.score())

# class Animal:
#     def __init__(self, name, legs):
#         self.name = name
#         self.legs = legs
#
#     def eat(self):
#         print("I can eat")
#
#     def no_of_legs(self):
#         print(f'I have {self.legs} legs')
#
# class Dog(Animal):
#     def eat(self):
#         print("I love eating meat")
#
#     def myName(self):
#         print(f'My name is {self.name}')
#
# class Cat(Animal):
#     def eat(self):
#         print("I love eating fish")
#
#     def myName(self):
#         print(f'I am a cat and my name is {self.name}')
#
# class Hen(Animal):
#     def no_of_legs(self):
#         super().no_of_legs()
#         
# labrador = Dog("Rohu", 4)
# # labrador.myName()
# labrador.eat()
#
# sylvia = Cat("Sylvia", 4)
# # print(sylvia.name)
# sylvia.eat()
#
# kuku = Hen("Kuku", 2) 
# kuku.no_of_legs()

# multiple inheritance
# class Mammal:
#     def mammal_info(self):
#         print("Breast feed their younger ones")
#
# class WingedAnimals:
#     def winged_animals_info(self):
#         print("Winged mammals have wings")
#
# class Bat(Mammal, WingedAnimals):
#     def __init__(self, name):
#         self.name = name
#
# bat = Bat("Bat")
# print(bat.name)
# bat.mammal_info()
# bat.winged_animals_info()
# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")
#
#     def make_sound(self):
#         print("Meow")
#
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")
#
#     def make_sound(self):
#         print("Bark")
#
# cat = Cat("Kitty", 2.5)
# dog = Dog("Fluffy", 4)
#
# for animal in (cat, dog):
#     animal.make_sound()
#     animal.info()
#     animal.make_sound()
# class Student:
#     def __init__(self, name):
#         self.name = name
#         
#     def __str__(self):
#         return f'The student\'s name is {self.name}'
#
# stud = Student("Ivy")
# print(stud)
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y 
#
#     def add_points(self, other):
#         x = self.x + other.x
#         y = self.y + other.y
#         return Point(x,y)
#
# p1 = Point(2,3)
# p2 = Point(4,5)
#
# p3 = p1.add_points(p2)
# print(p3.x, p3.y)

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y 
#
#     def __add__(self, other):
#         x = self.x + other.x
#         y = self.y + other.y
#         return Point(x,y)
#
# p1 = Point(2,3)
# p2 = Point(4,5)
#
# p3 = p1 + p2
# print(p3.x, p3.y)
# comparison operator overloading
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        return self.age < other.age

    def __eq__(self, other):
        return self.age == other.age

p1 = Person("Kevin", 20)
p2 = Person("Ivy", 19)
p3 = Person("Charity", 19)

print(p1 < p2)
print(p2 == p3)
