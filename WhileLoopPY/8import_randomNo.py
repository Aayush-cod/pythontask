import random

while True:
    a = random.randint(1,5)
    b = random.randint(1,5)
    print(a)
    print(b)
    c = a*b
    ans = int(input("Answer the multiple of a and b: "))

    if ans == c:
        print("Correct Answer!")
        ans = input("Do you want to continue?(yes/no)")
        if ans == 'yes':
            continue
        else:
            break
    elif ans != c:
        print("Incorrect Answer!")
        ans = input("Do you want to continue?(yes/no)")
        if ans == 'yes':
            continue
        else:
            break

        
       


   