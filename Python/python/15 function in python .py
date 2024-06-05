print ("defining a function (variables , parameterized)")

def gmean (a,b):
   gmean = (a*b)/(a+b)
   print (gmean)


print ("For first value")
a = 12
b = 2
gmean(a,b)

print ("For second value")
x = 34
y = 12
gmean(x,y)

print ("For third value ")
s= 10
f= 23
gmean (s,f)

print ("defining a function (non parameterized)")
def show():
   a=12
   b=112

   c=a+b
   print (c)


show()


print ("defining a function for if else ")

def isgreater (a,b):
   if (a>b):
      print ("first is greater ")
   else:
      print ("second is greater ")

q=12
w=113

isgreater(q,w)

def leave():
   pass




print ("defining a function (passing no as arguments)")

def takenum(a,b):
   print ("The sum is : ",a+b)


r=12
s=12

takenum(r,s)
takenum(2,4)