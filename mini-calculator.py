num1= float(input("enter your first number"))
num2=float(input("enter your second number"))
print("choose operation",end=": ")
print("+",end=",")
print("-", end=",")
print("*",end=",")
print("/")
choice=(input("Select your operation:"))
if choice=="+":
    print("Your answer is",num1+num2)
elif choice=="-":
    print("Your answer is",num1-num2)
elif choice=="*":
    print("Your answer is",num1*num2)
elif choice=="/":
    if num2==0:
        print("Invalid second number")
    else:
        print("Your answer is",num1/num2)
else:
    print( "invalid input")
    
