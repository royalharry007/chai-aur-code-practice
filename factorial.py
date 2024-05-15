number = int(input("enter the number you want factoiral : "))
factorial =1

while number>0:
    factorial=number*factorial
    number= number-1
    
    
print(factorial)