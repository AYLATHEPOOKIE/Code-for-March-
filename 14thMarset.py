set1={1,1,1,1,2,3,4}
print(set1)

set2=set()
print(type(set2))

#adding to sets

set1.add(314)
set1.remove(1)
set1.discard(12)
print(set1)

#set opperations

set3={1,2,3,4,5}
set4={4,5,6,7,8}

#union of sets

print(set3.union(set4))
print(set3|set4)

#intersection

print(set3.intersection(set4))
print(set3&set4)

#difference

print(set3.difference(set4))
print(set3-set4)
print(set4-set3)

#symmetric difference

print(set3.symmetric_difference(set4))
print(set3^set4)


#frozen
frozenset(set4)