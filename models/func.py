# print("Hello world!")
# def my_function(a,b):
#     my=(a+b)/(a*b)
#     print(my)
# a=10
# b=20
# my_function(a,b)
# def my_function1(a,b):
#     pass
# a=30
# b=50
# if(a<b):
#     print("a is less than b")
# else:
#     print("a is greater than b")
# my_function(a,b)
# # the two type functions available are in the python first is
# # 1. Built in function
# # 2. User define function.
# # def is a user defined function.

# pass the arguments in the function argument.
def my_function(name, mname='appy',lname="patil"):
    print("Hello, " + name, mname, lname)
my_function('Appu', 'alpya', 'pa')

# required arguments are function.
def my(a, b, c='appi'):
    print("Hello, ", a, b, c)
my('Appu','alpya')

# 3.keyword arguments in function.
def average(*number):
    print(type(number))
    sum=3
    # print("average is" , sum/len(number))
    return 2
    return sum/len(number)
a=average(122,13.3)
print(a)
def average1(**name):
    print("Hello, ", name['fname'], name['lname'], name['mname'])
average1(fname='tiger',lname='lion', mname='cat')