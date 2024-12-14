def find_lcm(num1, num2):
    if num1 > num2:
        greater = num1
    else:
        greater = num2

    while True:
        if greater % num1 == 0 and greater % num2 == 0:
            lcm = greater
            break
            greater += 1
    return lcm

def find_gcd(num1, num2):
    if num2 == 0:
        return num1
    else:
        return find_gcd(num2, num1 % num2)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("The LCM of", num1, "and", num2, "is", find_lcm(num1, num2))
print("The GCD of", num1, "and", num2, "is", find_gcd(num1, num2))