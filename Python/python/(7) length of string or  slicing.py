# to find the length of a string

names = "ali,aslam,irfan"

print (len(names))

fruit = "Mango"

len1 = len(fruit)

print (len1)

# to print length of string with silicing 

len2 = len(fruit[0:2])
len3 = len(fruit[:3])
len4 = len(fruit[:])

print (len2)
print (len3)
print (len4)

# FOR SLICING string 

print (fruit[:])

# for nagative slicing 

print ("For printing intials : ",fruit [0:-2])
print ("false : ",fruit [-1:-2])
print ("for printing last letters : ",fruit [-3:-1])