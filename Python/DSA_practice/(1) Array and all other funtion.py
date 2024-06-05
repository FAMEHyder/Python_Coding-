from array import *

# defining and printing  array

a1=array ('i', [1,2,3,4,5,6])
print  ("printing array in one row")
for i in a1:
    print (i,end = ' ')
print ("printing array in one colomn")
for i in a1:
    print (i)

# inserting element in array 
print ("array after insertion")

index = 0;
element = 0

a1.insert(index,element)

for i in a1:
    print (a1[i])

# removing from array
print ("Array after removing element")

a1.remove(0)

for i in a1:
    print (i)

# reverse element in array
print ("array after reversing element ")

a1.reverse()

for i in a1:
    print (i)

# appending array
print("array after appending ")

a1.append(7)

for i in a1:
    print (i)

# extending array
print ("Extending array")

a2 = array ('i', [8,9])

a1.extend(a2)

for i in range (len (a1)):
    print (a1[i])

    