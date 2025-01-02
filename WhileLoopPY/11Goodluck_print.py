goodluck_count = 0

while goodluck_count < 3:
        user_input = input("Enter a name or phrase: ")

        if user_input.lower() == "good luck":
          goodluck_count += 1
          if goodluck_count < 3:
                print(f"You typed the same word {goodluck_count} times.")
          else:
                print("You typed good luck three times.")
        else:
            print(f"You entered: {user_input}")

