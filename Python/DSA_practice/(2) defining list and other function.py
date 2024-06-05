list = ['Ali',12,55.5]

# To print list 
print ("printing list")
for s in list :
    print (s)


# To remove element from list
print ("To remove an element form list ")
list.remove(12)
for s in list :
    print (s)

# TO insert element in list 
index = 0;
element = 12

list.insert(index ,element)

print ("To insert element")

for x in list:
    print (x)

# To appand element in list
print ("after appanding list ")
list.append(34)

for c in list :
    print (c)


# To extend list
print ("List after extending ")
list2 = [11,22,33]
list.extend(list2)

for d in range (len(list)):
    print (list[d])

# To pop some thing in list 
print ("To pop some thing in list ")

element = list.pop(0)

print ("element is pop" ,element)

for f in list :
    print (f)

# To reverse list 
print ("your list is reversed")

list.reverse()

for d in list :
    print (d)