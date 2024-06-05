print ("passing required arguments in function")

def sum (a,b):
    print ("sun is :" , a+b)

a=12
b=12

sum(a,b)

sum(10,10)

print ("passing by default argument ")
def add (a=12,b=8):
    print ("sun is :" , a+b)

# if you pass an argument on calling the fubction it will ignore the by default arguments
    # you can also pass just one argument to the funxtion
add()

def getdata(name,subject):
    print ("The name is : ",name)
    print ("The subject is: ",subject)


getdata("saima","linear algebra")

print ("passing key word arguments")

def ston(a,b):
    print ("the value of a is :",a)
    print ("the value of b is : ",b)


ston(b=12,a=10)

print ("for variable lenght arguments")
def jod(*num):
    sum =0
    print (type(num))
    for i in num:
        sum =  sum+i
    print ("sum is :",sum)


jod(12,12,12,12,12,12,12,12)

print ("for dictionary arguments")

def dic(**name):
    pass
