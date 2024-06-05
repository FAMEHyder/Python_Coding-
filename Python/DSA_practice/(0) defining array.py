from array import *


# printing the value of array in one colomn 
print ("printing the value of array in one colomn ")
a1= array ('i',[1,2,3,4,5])

for x in a1:
    print (x)

# printing the value array in one row  
print ("printing the value of array in one row ")
for x in a1:
    print (x ,end = ' ')

# printing the index of array as addres 
print ("printing the index of array as addres ")
print (a1.index(1))    

# printing the value at given index
print ("printing the value at given index ")
print (a1[1])