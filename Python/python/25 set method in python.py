print ("Printing the unoin set ")

s = {1,2,3,4,5}
d = {3,4,5,6,7}
print (s)
print(d)
print (s.union(d))

print ("Printing the intersection of set")
print(s)
print(d)
print(s.intersection(d))


print("printing updated set")
s.update(d)
print (s,d)

f = s.symmetric_difference(d)
print (f)

q = s.difference(d)
print (q)

w = s.difference_update(d)
print(w)

o= d.intersection_update(s)
print (o)

y=s.isdisjoint(d)
print(y)

t=s.issuperset(d)

print(t)

g = s.issubset(d)

print(g)

s.add("ali")
print (s)

s.clear
print (s)

s.remove("ali")
print (s)

s.pop()
print (s)

s.discard
print (s)