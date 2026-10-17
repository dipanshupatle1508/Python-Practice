#Accept gender from user and print a greeting message.

gen = input("please enter your gender in (f or m) :-")

if gen=="M" or gen=="m" :
    print("good morning sir")
    
elif gen=="F" or gen=="f" :
    print("good morning mam")
    
else :
    print("please enter a valid input")