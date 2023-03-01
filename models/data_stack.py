def push(a,val):
    a.append(val)
    print("Insertion successfullly...")
def pop(a):
    x=a.pop()
    print("Poped item..", x)
    print("pop successfullly...")
def peek(a):
    index=len(a)-1
    # print("display successfullly...")
    print("peek Element", a[index])
def display(a):
    print("stack element are: ")
    for i in range(len(a)-1, -1, -1):
        print(a[i])
#create main function and programes
a=[]
print("Enter your choice")
while True:
    choice=int(input("1->push\n2->pop\n3->display\n4->peek\n5->Exit\n"))
    if choice==1:
        val=int(input("Entre the number of push..."))
        push(a,val)
    elif choice==2:
        if len(a)==0:
            print("Stack Underflow...")
        else:
            pop(a)
    elif choice==3:
        if len(a)==0:
            print("Stack Underflow...")
        else:
            peek(a)
    elif choice==4:
        if len(a)==0:
            print("Stack Underflow...")
        else:
            display(a)
    else:
        break

