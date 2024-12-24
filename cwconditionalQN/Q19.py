#To check login details.

username = str(input("Username:: "))
password = str(input('Password:: '))
if username == 'admin' and password == 'password123':
    print("Access Granted")
else:
    print("Access Denied")