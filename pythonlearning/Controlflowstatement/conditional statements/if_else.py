#if statement
pin=9283
print("welcome to atm!!!")
print ("please insert the card")
pinout=int(input("Enter the pin number"))
if pinout==pin:
    print("the amount want:")
else:
    print("wrong pin number!!!")