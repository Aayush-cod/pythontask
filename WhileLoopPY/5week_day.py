while True:
    user_input = str(input("Enter a day of a week:"))
    if user_input != 'sunday':
        print("It's not the weekend yet!")
        continue
    else:
        print("Enjoy your weekend!")
        break