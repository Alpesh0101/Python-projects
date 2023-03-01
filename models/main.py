# x=int(input('Enter the mathch case number to x: '))
# match x:
#     case 1:
#         print("my number is 1")
#     case 2:
#         print("my number is 2")
#     # case (x=12):
#     # case 12:
#     #     print("my number is 10")
#     # case 12:
#     #     print("my number is 12")

#     case _ if x!=12:
#         print("my number is 12")
#     case _ if x!=13:
#         print("my number is 13")
# used the for loop.
# name="Alpesh"
# for a in name:
#     print("my number is", a)
#     if(a=="l"):
#         print("my number is l is special character", a)
# color=["black", "blue", "green", "yellow"]
# for colors in color:
#     print("my number is", colors)
#     for b in colors:
#         print("my number is", b)
# # used the range() function.
# for i in range(1,12,4):
#     print(i)

# let discuss with the while loop with the python interpreter.
# a=0

import matplotlib.pyplot as plt
# plt.pie([1]) # Plot pie chart of value [1]
# plt.show() # To show Pie chart
classes = ["Python", 'R', 'Machine Learning', 'Artificial Intelligence', 
           'Data Sciece']
class1_students = [45, 15, 35, 25, 30]
plt.pie(class1_students, labels=classes)
# # plt.show()
figure=plt.figure(figsize=(6,4))
wedgeprops={"linewidth":4, "width":3, "edgecolor":"k"}
plt.pie( 
    class1_students,
    explode=None,
    labels=classes,
    colors=None,
    autopct="%0.2f%%",
    pctdistance=0.6,
    shadow=False,
    labeldistance=1.1,
    # starangle=0,
    radius=1,
    counterclock=True,
    wedgeprops=wedgeprops,
    textprops=None,
    center=(4, 2),
    frame=False,
    rotatelabels=False,
    normalize=True,
    data=None,
    # shadow=False
    )
explode = [0.03,0,0.1,0,0] # To slice the perticuler section
colors = ["c", 'b','r','y','g'] # Color of each section
textprops = {"fontsize":15} # Font size of text in pie chart
 
plt.pie(class1_students, # Values
        labels = classes, # Labels for each sections
        explode = explode, # To slice the perticuler section
        colors =colors, # Color of each section
        autopct = "%0.2f%%", # Show data in persentage for with 2 decimal point
        shadow = True, # Showing shadow of pie chart
        radius = 1.4, # Radius to increase or decrease the size of pie chart 
       startangle = 270, # Start angle of first section
        textprops =textprops) 
 
# plt.show() # To show pie chart only
plt.legend()
plt.show()