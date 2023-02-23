
# creating list
list1 = [1, "Hamza", 4, "Rasheed"]
list2 = []
list3 = list((1,2,3, 9))

print(list1)
print(list2)
print(list3)

# accessing list
list1=["hello",1,4,8,"good"]
print(list1)
list1[0]="morning"
# assigning values ("hello" is replaced with "morning")
print(list1)
print(list1[4])
print(list1[-2])
# list also allow negative indexing
print(list1[1:4]) # slicing
list2=["apple","mango","banana"]
print(list1+list2) # list concatenation
print(type(list2))

# built-in methods
list1=["apple","banana","grapes"]
list1.append("strawberry") # strawberry is added to the list
print(list1)
list1.pop() # removes the last element from the list
print(list1)
list1.pop(1)
print(list1)

#searching method
list1=[1,5,3,9,"apple"]
print(list1.index(9)) # returns the index value of the particular element
list2=[2,7,8,7]
print(list2.index(7)) # returns the index value of the element at its first occurence
print(list2.index(7,2)) # returns the index value of the element from the particular start position given