# # create the dictionaries and apply the all function.__annotations__
# My_dict={
#     20:"appu",
#     30:"appi",
#     40:"alpesh"
# }
# print(My_dict[30])
# # print the only for the keys.
# print(My_dict.keys())
# print(My_dict.values())
# # used the for loops.
# for key, value in My_dict.items():
#     print(f"the my dictionary keyis{key} and values{value} and{My_dict.keys()}")
# print(My_dict.items())

# # examples 2.
# ep={122:20, 123:60, 124:80}
# ep1={10:90, 20:80, 30:80, 40:80}
# # update the ep with ep1.
# ep.update(ep1)
# # ep.clear()
# # ep1={}
# # print(ep1)
# # remove the item in the your dictionary using the popitem() function.
# ep.popitem()
# ep.pop(123)
# # remove the last item in the dictionary using the popitem() function
# print(ep)
# # using the del() function.
# del ep1[123]
# print(ep1)

# used the for loop and used the else statement.
# for i in range(10):
#     print(i)
#     if i == 5:
#         break
# a=10
# # while a<6:
# #     a=a+1
# # else:
# #     print("i is not greater")

# # handling the Exception error handling function.
# a=int(input("Enter the value of the table"))
# print(f"Enter the value of the table{a}")
# # used the for loop.
# try:
#     for i in range(1,11):
#         # print(f"enter the{int(b)}X{i}={int(b)*i}")
# except:
#     print("sorry for the exception is stoped and show the error message")
# print("some lines of the code")
# print("some lines of the code")
# # create the second example.
# try:
#     num=int(input("Enter the number"))
#     c=[5,2]
#     print(c[num])
# except ValueError:
#     print("print the value error message")
# except IndexError:
#     print("print the index error message")
# # used the finally exception .
# finally:
#     print("print the finally exception")
# # create the second example.
# def func():
#     try:
#         a=[1,2,3,4]
#         b=int(input("Enter the function"))
#         return 1
#     except:
#         print("print the exception")
#         return 0
# # used the finally exception error and this methods used in the always solqve the finally exception error.
#     finally:
#         print("print the finally exception")
# print("print the the print function")

# d=func()
# print(d)

# create the custom function and solve the problem of custom errors.
# raising the custom errors.
# a=int(input("Enter the number of arguments and raising custom errors"))
# if (a<5 or a>10):
#     # print("enter the your first value")
#     raise ValueError("Enter the number of 5 and 10 its range")

# Exercise no.1
# kaun banega karror pati.
# Quetions=[["Enter you first answer"], 
# ["Enter your second answer"], 
# ["Enter your third answer"], 
# ["Enter your fourth answer", "Enter your"],
# ["Enter your third answer"]]
# # ["Enter your fourth answer", "Enter your"]]
# print(Quetions)
# levels=[10,100,1000,100000,1000000,1000000, 1000000000]
# # used the for loop.
# for i in range(0, len(Quetions)):
#     Quetions=Quetions[i]
#     print("Enter your first answer(level 1 t0 4)")
#     print(f"a.{Quetions[i]}   b.{Quetions[2]}  c.{Quetions[3]}   d.{Quetions[4]}")
#     reply=int(input("Enter your second answer 1-4"))
#     if reply==(Quetions[1]):
#         print("Enter your first answer{levels[i]}")
#         if(i==2):
#             print("You are won the first answer")
#             money=1000
#         elif(i==3):
#             print("You are won the first answer")
#             money=10000
#         # elif(i==6):
#         #     print("You are won the second answer")
#         #     money=100000
#         elif(i==4):
#             print("You are won the third answer")
#     else:
#         print("You are loss the first answer")
#         break

# used the short hand if and else statements,
# a=10
# b=12
# print(("A") if a<b else ("B") if a>b else ("C"))
# # stored the both conditions in one variables.
# c=8 if a>b else 0
# print(c)
# # create the second example.
# c=12
# d=9
# f=20
# print(("D") if d>c else print("E") if d>f else("F"))
# if a<b:
#     print("A")
# else:
#     print("B")

# create the enumerate function using the if and else statements.
marks=[12,13,14,15,16,17,18,19,20,21]
b=0
for a in marks:
    print(a)
    if(b==0):
        print("B")
    else:
        print("print the a")
    b+=1
for b, mark in enumerate(marks, start=2):
    print("print the enumerate function", mark)
    if(b==0):
        print("print the b")
    b+=1