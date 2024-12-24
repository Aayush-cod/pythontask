m = float(input("Enter your math's mark:" ))
n = float(input("Enter your nepali's mark:" ))
e = float(input("Enter your english's mark:" ))
c = float(input("Enter your computer's mark:" ))

total = m + n + e + c


per = (total / 400)*100


if 70 <= per <= 100 :
   grade= "Distinction!"
elif 60 <= per < 70 :
   grade= "First Divison!"
elif 40 <= per < 60:
   grade = 'Pass'
elif per < 40:
   grade = 'Fail!'

print('----RESULTS----')

print(f'Total marks: {total:.2f}')
print(f"Percentage: {per:.2f}%")
print(f'Grade: {grade}')
