import random
a = random.randint(1,10)
sum= 0
while True :
    
    

    guess = int(input("Guess the number:"))
    sum += 1
    if guess > a:
        print("Guess Lower!")
        
        continue
    elif guess< a:
        print("Guess higher!")
       
        continue
    elif guess == a:
        
        print(f'''Correct Answer.
              No of Attempts: {sum}
              
               ''')
        break