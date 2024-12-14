#Program that counts the number of tabs, spaces and newline characters in a file
filename='my_file.txt'
with open(filename) as file:
    text=file.read()
    tab_count=0
    space_count=0
    line_count=0
for char in text:
    if char=='\t':
        tab_count+=1
    elif char ==' ':
        space_count+=1
    elif char=='\n':
        line_count+=1
print("No. of Tabs   : ",tab_count)
print("No. of Spaces : ",space_count)
print("No. of Lines  : ",line_count)
