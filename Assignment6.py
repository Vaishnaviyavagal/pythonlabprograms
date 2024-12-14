#Program on operator overloading
class Complex:
    def __init__(self,val1,val2):
        self.real=val1
        self.imag=val2
    
    def Display(self):
        if(self.imag<0):
            print(self.real,"  ",self.imag,"i")
        else:
            print(self.real," + ",self.imag,"i")
    
    def __add__(self,other):
        temp=Complex(0,0)
        temp.real=self.real+other.real
        temp.imag=self.imag+other.imag
        return temp

print("Create First Complex Number")
x = float(input("Real part      : "))
y = float(input("Imaginary part : "))
c1=Complex(x,y)
print("Create Second Complex Number")
x = float(input("Real part      : "))
y = float(input("Imaginary part : "))
c2=Complex(x,y)
c3=Complex(0,0)
c3=c1+c2
c1.Display()
c2.Display()
c3.Display()
