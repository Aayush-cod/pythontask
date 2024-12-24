x = int(input("Enter the cost of your bike: "))

if x > 100000:
    print(f'Rs.{x}:: 15%')
elif 50000< x <= 100000 :
    print(f'Rs.{x}:: 10%')
elif x <= 50000:
    print(f'Rs.{x}:: 5%')