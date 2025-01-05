usernum = int(input('Enter a number: '))
i = 1
sum = 0
while i < usernum:
    if usernum % i == 0:
        sum += i
    i += 1
if usernum == sum:
    print('Given number is Perfect number.')
else:
    print('Given number is not Perfect number.')