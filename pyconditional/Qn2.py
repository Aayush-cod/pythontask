print("Welcome to treasure land!")

dir = str(input("Choose directions(left,right): "))

if dir == 'right':
    print('Game over !!!')

elif dir == 'left':
    opt = str(input('Choose options (swim, wait): '))
    if opt == 'swim':
        print("Game over !!")
    else:
        if opt == 'wait':
            col = str(input('Choose colors(red,blue,yellow): '))
            if col == 'red' or col == 'blue':
                print("Game over !!")
            else: 
                if col == 'yellow':
                    print('You win. yeahhh!!!!')
else:
    print('Invalid options!')