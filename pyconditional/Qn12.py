x = int(input("Enter the no of days you need to access the library: "))

if x <= 5:
    charge = x * 2
elif 6<= x <= 10:
    charge = x * 3
elif 11<= x <= 15:
    charge = x * 4
elif x > 15 :
    charge = x * 5
else:
    print("Invalid days!")

print(f"Your charge for {x} days: Rs.{charge}")