#Calculate the cube of all numbers from 1 to a given number

n=int(input("enter a number :-"))
cube = 1

for i in range(1,n+1,1):
    cube = i**3 
    print(cube)