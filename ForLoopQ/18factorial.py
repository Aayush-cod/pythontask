number = int(input("Enter a number: "))
fact = 1
for i in range(1,number+1):
    fact *= i
print("The factorial for ",number," is ",fact)