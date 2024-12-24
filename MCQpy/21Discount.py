price = eval(input("Enter the item's price: "))

if price > 1000:
    disprice =price- 0.2 * price 
    print(f"Your discounted price is : Rs{disprice} ")
elif price > 500 and price <= 1000:
     disprice = price-0.1 * price 
     print(f"Your discounted price is : Rs{disprice} ")
else:
     print("Invalid price range for discount!")