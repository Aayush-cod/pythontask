temp = float(input("Enter the temperature in degree celsius: "))

if temp > 30:
    print("It's hot, stay hydrated!")
elif 15 <= temp <= 30:
    print("Enjoy the weather!")
elif temp < 15:
    print("It's cold, wear warm clothes!")