
print ("itrating through normal way")
a = [1,2,3,4,5,6,7,8,9]

index =0
for i in a:
    print (i)
    if ( index == 4):
        
        print ('This is agent "Sahir"')
        
    index = index+1


print ("\n\n")
print ("itrating through enumrate")

b = [1,2,3,4,5,6,7,8,9]


for index,i in enumerate(b):
    print (i)
    if (index == 3):
        print ('This is agent "samar"')