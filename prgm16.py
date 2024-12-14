stack=[]
stack_size=5

def main():
    while True:
        print("Enter your choice")
        ch=int(input("1.Push\n2.Pop\n3.Display\n"))
        if ch==1:
            num=int(input("Enter number to be inserted::"))
            push_item(num)
        if ch==2:
            pop_item()
        elif ch==3:
            display()
        else:
            print("Invalid choice")
            val=input("Do you want to continue(Yes/No)::")
            if val=='No':
                break
            
def push_item(item):
    if(len(stack)<stack_size):
        stack.append(item)
    else:
        print("stack is full")

def pop_item():
    if(len(stack)>0):
        print(f"Item_Deleted={stack.pop()}")
    else:
        print("stack is Empty")
        
def display():
    print("Elements of stack are:")
    for i in stack:
        print(i)
        
if __name__=="__main__":
    main()


