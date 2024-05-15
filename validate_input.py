
# keep asking the user for input until the user enter the number between 1 to 10

while True:
    num = int(input("enter the number between 1 to 10 : "))
    if (num>=1 and num<=10):
        print("thank you")
    else:
        print("invalid number try again : ")
    
    