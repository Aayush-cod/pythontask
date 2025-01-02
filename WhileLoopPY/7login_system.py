username = 'admin'
password = '123'
attempt = 0

while True:
    attempt += 1

    if attempt == 4:
        print("Too many failed attempts. Try again later!")
        break
   
    

    username1 = input('Enter your username:')
    pass1 = input("Enter your password:")
    

   
    if username1 != username or pass1 != password:
        print("Invalid credentials, try again.")
        continue
    elif username1 == username or pass1 == password:
        print("Login successful!")
        break