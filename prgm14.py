list_item=[]

def main():
    n=int(input("Enter the number of items to be inserted::"))
    for i in range(n):
        num=int(input("Enter a number::"))
        list_item.append(num)
    print(list_item)
    key=int(input("Enter the element to be searched::"))
    linearSearch(list_item,key)
    
def linearSearch(list_item,key):
    found=False
    for i in range(len(list_item)):
        if list_item[i]==key:
            found=True
            break
    if found==True:
        print(f'{key} is present at location')
    else:
        print(f'{key} is not present')
        
if __name__=="__main__":
    main()

        
    