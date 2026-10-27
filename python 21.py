#Reverse a string without using built-in functions.

var = "python"
rev =""

for i in range(len(var)-1,-1,-1):
    
    rev = rev + var[i]
    
print(rev)