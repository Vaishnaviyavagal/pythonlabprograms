'''Program that stores the information about student like roll no, name & marks
of three subjects. Display the result based on the following criteria
================================
% of Marks          Result
================================
>=75.00             Distinction
60.00 to 74.99      First Class
50.00 to 59.99      Second Class
40.00 to 49.99      Pass Class
<=39.99             Fail'''
class Student:
    def __init__(self,rl,nm,lst):
        self.Name=nm
        self.Roll_No=rl
        self.__M=lst
    def Result(self):
        total=self.__M[0]+self.__M[1]+self.__M[2]+self.__M[3]+self.__M[4]
        self.avg=total/5.0
        if(self.__M[0]<40 or self.__M[1]<40 or self.__M[2]<40 or self.__M[3]<40 or self.__M[4]<40):
            self.result="Fail"
        elif(self.avg>=75.00):
            self.result="Distinction"
        elif(self.avg>=60.00 and self.avg<75.00):
            self.result="First Class"
        elif(self.avg>=50.00 and self.avg<60.00):
            self.result="Second Class"
    def Display(self):
        print("Roll No. : ",self.Roll_No)
        print("Name     : ",self.Name)
        i=1
        for m in self.__M:
            print("Subject",i,":",m)
            i+=1
        print("Result : ",self.result)

print("Enter the details of the student")
r = int(input("Roll Number : "))
n = input("Name : ")
lst=[]
print("Marks of 5 subjects")
for i in range(1,6):
    m = int(input())
    lst.append(m)
std = Student(r,n,lst)
std.Result()
std.Display()
