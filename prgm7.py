lower=int(input("Enter the value::"))
upper=int(input("Enter the value::"))
print(f"prime number between {lower} + {upper} are ::")

for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if (num % i)==0:
                break
        else:
            print(num)