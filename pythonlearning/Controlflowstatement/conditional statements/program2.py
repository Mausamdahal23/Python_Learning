# if elif
print("choice1:withdraw"
      "choice2:balance check"
      "choice3:deposit")
choice=int(input("enter the choice"))
if choice==1:
    print("enter the amount")
elif choice==2:
    print("your balance is")
elif choice==3:
    print("deposit your amount")
else:
    print("wrong choice")