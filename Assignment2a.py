#Program to demonstrate the working of stack using list
stack=[]
while True:
    print("1.Push\n2.Pop\n3.Exit")
    choice = int(input("Enter your choice : "))
    if(choice==1):
        element=int(input("Enter the element to be pushed : "))
        stack.append(element)
        print(stack)
    elif(choice==2):
        if(len(stack)==0):
           print(stack)
        else:
            print("Deleted element is ",stack.pop())
            print(stack)
    else:
        exit();
        
