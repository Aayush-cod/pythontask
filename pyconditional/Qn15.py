#students desk no. question

a = int(input("Enter the number of students in class 1: "))
b = int(input("Enter the number of students in class 2: "))
c = int(input("Enter the number of students in class 3: "))

if a % 2 == 0:
    desks_a = a // 2
else:
    desks_a = (a // 2) + 1

if b % 2 == 0:
    desks_b = b // 2
else:
    desks_b = (b // 2) + 1

if c % 2 == 0:
    desks_c = c // 2
else:
    desks_c = (c // 2) + 1
total_desks = desks_a + desks_b + desks_c
print(f"Total Desk needed is: {total_desks}")