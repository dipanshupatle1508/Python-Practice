import random

com =(random.randint(1,100))
tries = 0
while True:
    
    tries +=1
    hum =int(input("enter a number (btw 1-100) :-"))
    
    if hum == com :
        print(f"congratulations you won in {tries} tries")
        break
    elif hum > com :
        print("enter value lower")
        
    elif hum < com :
        print("enter value higher")
        
    