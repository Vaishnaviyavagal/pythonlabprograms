num=int(input("Enter a value::"))
fact=1
if num<0:
    print("factorial does not exist")
elif num==0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,num):
        fact=fact*i
    print(f"The factorial or {num} is {fact}")