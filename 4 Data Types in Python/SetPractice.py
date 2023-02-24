#creating set
set1={1,2,3,4,5,"hello","tup"}
set2={(1,8,"python",7), ("hamza"), ("w",2), (1,2,3,4,5)}
set3 = {}
print(set1)
print(set2)
print(set3)

#accessing set
set1={1,2,3,4,5}
print(set1)
#print(set1[0]) #sets are unordered, so it doesnot support indexing
set2={3,7,1,6,1} # sets doesnot allow duplicate values
print(set2)

#built-in methods
set1={"water","air","food"}
set1.add("shelter") # adds an element to the set at random position
print(set1)
set1.add("clothes")
print(set1)
set1.pop() # removes random element from the set
print(set1)

#searching method
set1={1,5,6,3,9}
# set1.index(5)# will throw an error as they are unordered