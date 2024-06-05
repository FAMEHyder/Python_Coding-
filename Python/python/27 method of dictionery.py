ep1 ={100:79,101:34,102:78}

ep2 ={103:89,104:99}
print("printing the updated dic")
ep1.update(ep2)
print (ep1)

print("clear the dic")
ep2.clear()
print (ep2)

print("printing the empty dic")
y = {}
print(y)

print("pop the given value")
ep1.pop(100)
print (ep1)

print("pop the last item")
ep1.popitem()
print(ep1)

print ("delete the value")
del ep1[101]
print(ep1)