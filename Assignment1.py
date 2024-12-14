#Program to calculate the Net salary of an employee based on the designation
Name = input("Enter the name of an employee : ")
Basic = float(input("Enter the basic salary of an employee : "))
print("1.Manager\n2.Clerk\n3.Assistant")
Designation = int(input("Enter the designation type : "))
if(Designation == 1):
	DA  = Basic*127/100
	HRA = Basic*17/100
	Gross = Basic+DA+HRA
	Gross_temp=Gross*12
	if( Gross_temp<= 750000):
		IT=Gross*5.75/100
	elif( Gross_temp> 750000 and Gross_temp<=1000000 ):
		IT=Gross*6.25/100
	elif( Gross_temp> 1000000 and Gross_temp<=1200000 ):
		IT=Gross*6.75/100
	else:
		IT=Gross*7.5/100
elif(Designation == 2):
	DA  = Basic*107/100
	HRA = Basic*12/100
	Gross = Basic+DA+HRA
	Gross_temp=Gross*12
	if( Gross_temp>= 500000):
		IT=Gross*5.0/100
	elif( Gross_temp> 500000 and Gross_temp<=750000 ):
		IT=Gross*5.35/100
	elif( Gross_temp> 750000 and Gross_temp<=1000000 ):
		IT=Gross*5.75/100
	else:
		IT=Gross*6.0/100
elif(Designation == 3):
	DA  = Basic*97/100
	HRA = Basic*10/100
	Gross = Basic+DA+HRA
	Gross_temp=Gross*12
	IT=0
	if( Gross_temp>= 750000):
		IT=Gross*5.25/100
Net_Salary=Gross-IT
print("Name : ",Name,"\nDesignation : ",Designation,"\nBasic",Basic,"\nNet Salary : ",Net_Salary)
