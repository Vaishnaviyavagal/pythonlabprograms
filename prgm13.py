list_item=[]

def main():
    n=int(input("Enter the number of items to be inserted::"))
    for i in range(n):
        num=int(input("Enter a number::"))
        list_item.append(num)
        print(list_item)
    calculate(list_item)
    
def calculate(list_item):
    sum_positive=0
    sum_negative=0
    for i in range(len(list_item)):
        if list_item[i]>0:
            sum_positive=sum_positive+list_item[i]
        else:
            sum_negative=sum_negative+list_item[i]
    print(f"sum of Positive Number={sum_positive}")
    print(f"sum of Negative Number={sum_negative}")
    
if __name__=="__main__":
    main()