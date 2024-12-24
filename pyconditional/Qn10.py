x = int(input("Enter your grade in number: "))

if x > 80:
    print('A+')
elif 60 < x <= 80:
    print('A')
elif 50< x <= 60:
    print('B+')
elif 45 < x <= 50:
    print('B')
elif 25 <= x <= 45:
    print('C')
elif x < 25:
    print('D')

