#Accept name and age — check if the user is a valid voter (18+).

name = input("enter your full name :-")
age= int(input("enter you current age :-"))

if age>=18 :
    print("you are eligible to vote")
    
else :
    print("you are not eligible to vote")