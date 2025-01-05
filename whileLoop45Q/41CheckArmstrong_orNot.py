usernum = input('Enter a number: ')
i = armnum = 0
power = len(usernum)
while i < len(usernum):
    armnum += int(usernum[i])**power
    print(armnum)
    i += 1
if int(usernum) == armnum:
    print('The number is armstring')
else:
    print('The number is not armstring')
    