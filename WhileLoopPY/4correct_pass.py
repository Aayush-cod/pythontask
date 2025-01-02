while True:
    password = 'open sesame'
    user_input = input("Enter your password:")
    if user_input != 'open sesame':
        print("Wrong password,Try Again!")
        continue
    else:
        print("Access Granted!")
        break