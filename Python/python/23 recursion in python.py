# to the factorial of any num we need to do the fallowing
print ("Printg the factorial of a number")

def factorial (n):
    if (n==0 or n==1):
        return 1
    else :
        return n*factorial(n-1)


print (factorial(3))
print (factorial(4))
print (factorial(5))