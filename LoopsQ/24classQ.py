
username = "Aayush"
password = "1234"

for i in range(3,0,-1):
    user1 = input("Enter your valid username: ")
    pass1 = input("Enter your valid password: ")
    if ( 
         username != user1 or password != pass1 or len(pass1) < 8 or user1 == '' or pass1 == ''


    ):
        if i == 1:
            continue
        print(i-1,"Attempt left!")
    else:
        print("You have loged in successfully!")
        break
else:
        print("You are blocked!")
    