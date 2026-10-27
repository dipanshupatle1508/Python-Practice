#Count letters, digits, and special symbols in a string.


a = "P@#yn26at^&i5ve"
char = 0
special=0
digits=0

for i in a :
    if i.isdigit() :
        digits = digits +1 
    elif i.isalpha():
        char = char + 1
    else :
        special = special + 1
        
print(f"characters = {char} , special character = {special} , digits = {digits} ")