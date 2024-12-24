#Takes a month in number and outputs corresponding season.

mon = int(input('Enter any number between (1-12):  '))

if mon in [12,1,2]:
    print('Winter')

if mon in [3,4,5]:
    print('Spring')

if mon in [6,7,8]:
    print('Summer')

if mon in [9,10,11]:
    print('Autumn')

