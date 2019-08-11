n = int(input("Please input a positive integer number larger than 2:\n"))
x = 2
prime = True

if n <= 0 :
    prime = False

while x <= n/2 :
    if n%x == 0:
        prime = False 
    x = x + 1

if prime == True:
    print("It is a prime number.")
else:
    print("It is not a prime number.")
    
    
    
