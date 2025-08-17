roomates={'achal':120,'anushka':57,'sayli':129}
print(type(roomates))
roomates['bhumika']=52
print(sorted(roomates))
del roomates['sayli']
print(roomates)
print(list(roomates))
print('anushka' in roomates)
print('achal' not in roomates)

weight=dict([('achal', 52),('anushka',35),('sayli',54)])
print(type(weight))


#creating dict from arbitary key valur pair
squares={x: x**2  for x in (2,4,6)}
print(squares)

#Looping techniques
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for key,value in knights.items():
    print(key,value)
d = {"one": 1, "two": 2, "three": 3, "four": 4}
print(d) # shows dictionary
print(list(d)) # by default it only takes keys # list(d) == list(d.keys())

print(d.values()) #for only values 
print(d.items()) #key value pairs as tuples
del d['two']
print(d)
d["two"]=None
print(len(d))
#print(d['five']) #keyerror

print(iter(d))#walks through keys one-by-one
print(list(d))# collects all keys
print(d['two']) #jumps straight to the value
print(iter(d.values())) #values
print(iter(d.items())) # key value pairs
print(d.get('five')) # doesnt raise error but map doesnt find
print(d.popitem())
print(d)
#print(d.clear())
print(list(reversed(d)))
d.update([knights])
print(d)

b={'a':1}
v=b.values()
print(v)
b['c']=2
print(v)
print(d.values()==d.values())#Every call to d.values() creates a new view object (even if it’s on the same dict).
print(list(d.values()) == list(d.values()))#If you actually want to compare the values

