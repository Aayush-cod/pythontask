choice= str(input("Are you veg or non-veg(veg/non-veg)?:"))

if choice == "veg":
    opt = str(input("What do you want(salad/pasta)?: "))
    if opt == 'salad':
        print("Your salad is on the way!")
    if opt == "pasta":
          print("Your salad is on the way!")

elif choice == "non-veg":
      opt = str(input("What do you want(chicken/fish)?: "))
      if opt == 'chicken':
        print("Your chicken is on the way!")
      if opt == "fish":
          print("Your fish is on the way!")

else:
    print("Invalid INput!")
     

