list1 = [1,2,3]
list2 = [3,1,4]
list3 = []

for i in list1:
    for x in list2:
        if x != i:
            list3.append((i,x))
print(list3)

list4 = [(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(list4)