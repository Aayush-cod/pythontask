timeperiod = int(input("How many years you have been in the company: "))
salary = int(input("How much is your salary: "))

if timeperiod > 5:
    print(f"For {timeperiod} years, bonus is Rs.{salary * 0.05}")
else:
    print("Sorry, Not enough years of service! So No bONUS this time")