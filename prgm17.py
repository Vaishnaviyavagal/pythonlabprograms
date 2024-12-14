string = "Hello, World!"
length = len(string) 
print("Length of the string:", length)
uppercase = string.upper()
print("Uppercase string:", uppercase)
lowercase = string.lower()
print("Lowercase string:", lowercase)
count=string.count("o") 
print("Number of 'o' in the string:", count) 
 
my_list=[1,2,3,4,5]
length=len(my_list)
print("Length of the list:", length) 
my_list.append(6) 
print("List after appending element:", my_list)
my_list.sort()
print("Sorted list:", my_list)
my_list.reverse() 
print("Reversed list:", my_list) 
 
my_dict = {"name": "John", "age": 25, "city": "New York"}
length = len(my_dict) 
print("Length of the dictionary:", length)
keys=my_dict.keys() 
print("Keys in the dictionary:", keys) 
 
values = my_dict.values()
print("Values in the dictionary:", values)
key_exists = "age" in my_dict 
print("Does 'age' exist in the dictionary?", key_exists)
my_dict.pop("age") 
print("Dictionary after removing 'age:", my_dict) 
 
