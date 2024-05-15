# if the age is greater than 18 the ticket price is 12$ and if it is less than 18 price will be
# 8$ and there will be 2$ discount on wednesday

age =int(input("Enter your age : "))

day ="wednesaday"

price =12 if age<18 else 8

if day=="wednesaday":
    price = price-2
print(price)


