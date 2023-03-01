# create the Water, Snake and Gun game in python.
# this game working on the computer and computer user.
import random
def comp(computer, user):
    if computer==user:
        return 0
    if (computer==0 and user==1):
        return -1
    if (computer==1 and user==0):
        return -1
    if (computer==3 and user==2):
        return -1

comit=random.randint(1,10)
# print(computer)
rand=int(input("Enter the computer random numbers"))
# print(rand)
score=comp(comit, rand)
print("computer: ", comit)
print("User: ", rand)
if (score==-1):
    print("you is lose")
elif(score==2):
    print("you are winning")
else:
    print("both are lost")