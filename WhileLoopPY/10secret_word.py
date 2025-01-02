
password = 'python'


while True:
    
    guess = input("Guess the word: ")

    if guess != password:
        print('Incorrect,Try again!')
        
        guess = input("Do you want to continue?(y/n)")
        if guess == 'y':
            continue
        else:
            break
            
             
    else:
        print("Congratulations, you guessed the word!")
        break



   

   
    