# check the multiplication table for the given number upto 10 , but skip the fifit iteration

number =int(input("enter the number for multiplication : "))

for num in range(1,11):
    if num==5:
        continue
    print(f"{number} x {num} = ", number*num)
  