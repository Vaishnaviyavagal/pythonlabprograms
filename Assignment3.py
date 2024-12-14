#Function to calculate the factorial
from math import pi
def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f


#Function to calculate the expenent value
def exp(x,y):
    ans=1
    for i in range(1,y+1):
        ans=ans*x
    return ans

#Program to calculate the value of sin using series
n = int(input("How many iterations?\n"))
x = int(input("Enter the value of x : "))

a=3
sign=-1
y=x
x=x*(pi/180)
sin=x

for i in range(1,n):
    sin=sin+(exp(x,a)/fact(a))*sign
    sign=sign*(-1)
    a=a+2
print("i = ",i)
print("Sin(",y,") = ",sin)
