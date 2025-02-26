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
class Rectangle:
    width = 0
    length = 0

    def area(self):
        return f'The area of the rectangle is {self.width * self.length}'

rect1 = Rectangle()
rect1.width = 2
rect1.length = 5
print(rect1.area())

