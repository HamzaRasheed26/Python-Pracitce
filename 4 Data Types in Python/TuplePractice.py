#creating tuple
tuple1=(1,2,"college",9)
tuple2=() # creates an empty tuple
tuple3=tuple((1,3,5,9,"hello"))

print(tuple1)
print(tuple2)
print(tuple3)

# accessing tuple
tuple1=("good",1,2,3,"morning")
print(tuple1)
print(tuple1[0]) # accessing values using indexing
#tuple1[1]="change" # a value cannot be changed as they are immutable
tuple2=("orange","grapes")
print(tuple1+tuple2) # tuples can be concatenated
tuple3=(1,2,3)
print(type(tuple3))

# built-in functions
tuple1=(1,2,3,4)
# tuple1.pop() tuple cannot be modified
# tuple1.append() tuple cannot be modified
print(tuple1)

#searching method
tuple1=(1,3,6,7,9,10)
print(tuple1.index(6)) #prints 2
print(tuple1.index(9)) #prints 4