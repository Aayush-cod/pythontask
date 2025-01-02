

while True:
    age = eval(input('Enter your age: '))

    if age < 18:
        print("You are a minor.")
        age = input('Do you want to check again?(yes/no)')
        if age == 'yes':
            continue
        else:
            break
    elif age>= 18 or age<=60:
        print('You are an adult.')
        age = input('Do you want to check again?(yes/no)')
        if age == 'yes':
            continue
        else:
            break
        
        
    elif age > 60:
        print('You are a senior citizen.')
        age = input('Do you want to check again?(yes/no)')
        if age == 'yes':
            continue
        else:
            break
        
   