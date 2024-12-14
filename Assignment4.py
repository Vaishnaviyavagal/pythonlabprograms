#Write a Program that pluralize the each word using regular expression
import re
def plural(noun):
    if re.search('[sxz]$',noun):
        return re.sub('$','es',noun)
    elif re.search('[^aeioudgkprt]h$',noun):
        return re.sub('$','es',noun)
    elif re.search('[^aeiou]y$',noun):
        return re.sub('y$','ies',noun)
    else:
        return noun + 's'

n=int(input("How many nouns?"))
List=[]
for i in range(n):
    print("Word ",i+1," : ",end='')
    word = input()
    List.append(word)
for i in List:
    print(i,'-',plural(i))
