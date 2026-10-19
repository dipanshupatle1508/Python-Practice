#find smallest of three number 

num1 = int(input("please enter first number :-"))
num2 = int(input("enter seconf number :-"))
num3 = int(input("enter third number :-"))

if num1>num2 and num1>num3 :
    print(f"{num1} is greatest number")
    
elif num2>num1 and num2>num3:
    print(f"{num2} is greatest number")
    
elif num1==num2 and num2==num3 :
    print("all three numbers are same")
    
else :
    print(f"{num3} is greatest number")

#solved