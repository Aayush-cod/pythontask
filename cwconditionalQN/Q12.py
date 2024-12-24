a = input("Enter any character: ")

if a.isupper():
    print("Uppercase!")
elif a.islower():
    print("Lowercase!")
elif a.isdigit():
    print("Digit!")
else:
    print("It is neither of them.")