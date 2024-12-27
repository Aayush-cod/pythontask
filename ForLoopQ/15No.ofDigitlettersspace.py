user_string= input("Enter any string: ")

digit = 0
alpha = 0
space = 0

for i in user_string:
    if i.isdigit():
        digit += 1
    elif i.isalpha():
        alpha +=1
    elif i.isspace():
        space += 1

print(f"Number of digits: {digit}")
print(f"Number of letters: {alpha}")
print(f"Number of spaces: {space}")