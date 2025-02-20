# print("hey now brown cow", end='\t')
# print("Mr President")
# print("Bush", "Obama", "Clinton", sep=", ")
# pres44 = "Barack Obama"
# pres45 = "Donald Trump"
#
# print('President {} came before President {}'.format(pres44, pres45))
# first_num = int(input("Enter first number: "))
# second_num = int(input("Enter second number: "))
# sum = first_num + second_num
# print('The result of adding {} and {} is {}'.format(first_num, second_num, sum))

# x1 = 5
# y1 = 6 
# x2 = 'Hello'
# y2 = 'Hello'
# x3 = [1,2,3]
# y3 = [1,2,3]
#
# print(x3 is not y3)
def bill_split(amount, friends):
    amount *= 1.2
    return amount / friends

amount = int(input("Enter the amount: "))
friends = int(input("How many of you are there: "))

print(bill_split(amount, friends))
