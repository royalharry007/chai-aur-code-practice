# if the age is greater thean 13 he is child and if the ages is range between (13-19) he is teenger and if the age is range between (19-59) print adult and age more than that is senior 

age = int(input("enter the your age "))

if age<13:
    print("your are child")
elif age>=13 and age<19:
    print("your are teenger")
elif (age>=19) and (age<59):
    print("your are adult")
else:
    print("you are senior")