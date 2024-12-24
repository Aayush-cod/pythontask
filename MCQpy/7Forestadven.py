welcome_screen= '''

Welcome to the Forest Adventure!
please select:
1. Left
2. Right

'''

Invalid = "Inavlid option!"

user_choice = int(input(welcome_screen))

if user_choice == 2:
    print("You fell inot a trap.Game over!")
elif user_choice == 1:
    opt_Sec = int(input('''
      Choose between:
      1.explore
      2.rest

    '''
    ))
    
    if opt_Sec == 1:
          print("You found treasure!")
    elif opt_Sec == 2:
           print("You were attacjed by wild animals.Gmae over!")
    else:
          print(Invalid)

else:
    print(Invalid)