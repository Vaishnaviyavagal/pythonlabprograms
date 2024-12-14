import cmath
a=int(input("Enter the value ::"))
b=int(input("Enter the value ::"))
c=int(input("Enter the value ::"))

d=(b**2)-(4*a*c)

sol1=(-b+cmath.sqrt(d))/(2*a)
sol2=(-b-cmath.sqrt(d))/(2*a)

print(f"The two roots of the above Quadratic equation is ::{sol1} & {sol2}")
