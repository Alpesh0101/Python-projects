# Health Management System
def getDate():
    import datetime
    return datetime.datetime.now()


# converting the return value of the getDate() function into a string in order to add them to the exercise/diet name
date = str(getDate())


# defining a function for setting exercise/diet food for a client
def setTips(clientName):
    print("Press 1 for Exercise")
    print("Press 2 for Diet")
    trainInp = int(input("Enter a number among 1/2: "))
    if trainInp == 1:
        exerciseInp = input("write exercise for Client {}: ".format(clientName))
        if not exerciseInp.isnumeric():
            filePointerSetExer = open("Client{}Exercise.txt".format(clientName), "a")
            filePointerSetExer.write("[" + date + "]" + " " + exerciseInp + "\n")
            filePointerSetExer.close()
        else:
            print("please write a valid exercise name!!")
    elif trainInp == 2:
        foodInp = input("Write diet food for Client{}: ".format(clientName))
        if not foodInp.isnumeric():
            filePointerSetFood = open("Client{}Food.txt".format(clientName), "a")
            filePointerSetFood.write("[" + date + "]" + " " + foodInp + "\n")
            filePointerSetFood.close()
        else:
            print("Please write a valid food name !!")
    else:
        print("You have entered an invalid number !!")


# defining a function for getting the existing instruction about a client
def getTips(clientIndex):
    print("Press 1 for Exercise")
    print("Press 2 for Diet")
    tipsInp = int(input("Enter a number among 1/2: "))
    if tipsInp == 1:
        filePointer = open("Client{}Exercise.txt".format(clientIndex), "rt")  # writing rt is optional here
        fileContentExer = filePointer.read()
        print(fileContentExer)
        filePointer.close()
    elif tipsInp == 2:
        filePointerClient = open("Client{}Food.txt".format(clientIndex), "rt")  # writing rt is optional here
        fileContentFood = filePointerClient.read()
        print(fileContentFood)
        filePointerClient.close()
    else:
        print("Please enter a number among 1/2!!")


startingInp = input('Enter \'S\' to Set Exercise/diet or \'G\' to Get Existing\nInstructions: ')
if startingInp == 'S':
    print("Press 1 for Client 1")
    print("Press 2 for Client 2")
    print("Press 3 for Client 3")
    # this input box will decide the client name for whom we have to set the instructions
    nameInp = int(input("Enter a number among 1/2/3: "))
    if nameInp == 1 or nameInp == 2 or nameInp == 3:
        # calling the setTips() function
        setTips(nameInp)
    else:
        print("You have entered invalid number !!")
elif startingInp == 'G':
    print("Press 1 for Client 1")
    print("Press 2 for Client 2")
    print("Press 3 for Client 3")
    # this input box will decide the client name for whom we have to retrieve the data
    clientIndexInp = int(input("Enter a number among 1/2/3: "))
    if clientIndexInp == 1 or clientIndexInp == 2 or clientIndexInp == 3:
        # calling the getTips() function
        getTips(clientIndexInp)
    else:
        print("You have entered an invalid number!!")
else:
    print("Please enter either S or G !!")

