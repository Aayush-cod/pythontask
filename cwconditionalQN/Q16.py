a = input("Enter your choice(pizza, burger, pasta): ")

if a == 'pizza':
    print(f'{a}: $10')
elif a == 'burger':
    print(f'{a}: $7')
elif a == 'pasta':
    print(f'{a}: $8')
else:
    print("Not Available right now!")
