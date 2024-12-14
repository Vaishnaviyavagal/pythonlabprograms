val=input('Enter the string::')
count=0
val=val.lower()
for i in val:
    if i== 'a' or i=='e' or i=='i' or i=='o' or i=='u':
         count+=1  
if count == 0:
    print('No vowels found')
else:
    print('Total vowels are :',count)
    
print(f'Total number of letters::{len(val)}')
    