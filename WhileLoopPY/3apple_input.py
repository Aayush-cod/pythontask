while True:
    user_input = str(input("Enter a fruit name:"))
    if user_input != 'apple':
        print("Try Again!")
        continue
    else:
        print("You got it!")
        break