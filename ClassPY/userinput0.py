a = int(input("Enter any number:"))
sum=0
while a != 0:
    sum = sum + a
    print(sum)
    a = int(input("Enter any number again:"))
else:
    print('Its zero.')