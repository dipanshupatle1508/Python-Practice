#Separate each digit of a number and print on a new line.

n =int(input(" enter your number :-"))

while n > 0 :
    print(n%10)
    n=n//10