usernum = int(input('Enter a number: '))
count = 0
i = 1
while i <= usernum:
    if usernum % i == 0:
        count += 1
    i += 1
if count == 2:
    print('Given number is prime.')
else:
    print('Given number is not prime.')