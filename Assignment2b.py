Marks={'Neha':[97,98,94,61],'Mithila':[67,89,78,98],'shifali':[89,91,97,94]}
tot=0
Tot_Marks=Marks.copy()
for key,val in Marks.items():
    tot=sum(val)
    Tot_Marks[key]=tot
print(Tot_Marks)
max=0
Topper= ''
for key,val in Tot_Marks.items():
    if val>max:
        max=val
        Topper=key
print("Topper is :",Topper,"with marks=",max)
