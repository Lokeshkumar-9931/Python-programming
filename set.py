set1={2,4,6576,4,2,4,5,7,8}
print(set1)
set2={"lokesh",12,76,12,"lokesh"}
print(set2)

empty_set=set()
print(type(empty_set))

for i in set2:
    print(i,end=" ")
print("\n")   
#set methods
s={2,3,4}
s2={3,6,7}
print(s.union(s2))    
print(s.intersection(s2))    
s.update(s2)
print(s,s2)

cities={"jaipur","patna","gaya","jehanabad","alwar"}
city={"raipur","banglore","mumbai","delhi","patna","gaya"}
city.update(cities)
print(city,cities)
print(city.union(cities))
print(city.intersection(cities))
print(city.intersection_update(cities))
print(city.difference(cities))
print(city.symmetric_difference_update(cities))
print(city.difference_update(cities))
print(city.isdisjoint(cities))
print(city.issuperset(cities))
print(city.issubset(cities))
city.add("mathura")
print(city)
print(type(city))
#city.remove("delhi")
city.discard("delhi")
print(city)
#del city
city.clear()
print(city)
