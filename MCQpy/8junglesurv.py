welcome_n = '''
Welcome to the Jungle Survival Challenge!!

please choose:

1. search for food
2. build a shelter

'''
Invalid = "INvalid option!"

user_c = int(input(welcome_n))

if user_c == 2:
    print("Your shelter collapsed in rain. Game Over!")
elif user_c == 1:
    opt_u = int(input('''
                 Choose options:

                      1. hunt
                      2. gather     
                      
                      
                     ''' ))
    if opt_u == 1:
        print("You were attacked by a wild animal.Game Over!")
    elif opt_u == 2:
        print("You found enough food.You win!")
    else:
        print(Invalid)
else:
    print(Invalid)
    