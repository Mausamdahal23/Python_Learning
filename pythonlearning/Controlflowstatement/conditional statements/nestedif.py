#nested if else
pin=9807
balance=2000
print("choice1: balance enquiry")
print("choice2: cash withdraw")
print("choice3: cash deposit")
choice=int(input("enter your choice"))
if choice==1:
    print("your balance is:",balance)
elif choice==2:
    amount=int(input("enter the amount:"))
    if amount<= balance:
        print("kiririririr")
    else:
        print("insufficient balance")
elif choice==3:
    print("deposit yoru ampount:")
else:
    print("invalid choice")