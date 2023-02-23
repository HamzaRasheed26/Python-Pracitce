#creating dictionary object
dict1={"key1":"value1","key2":"value2"}
dict2={} # empty dictionary
dict3=dict({1:"apple",2:"cherry",3:"strawberry"})
print(dict1)
print(dict2)
print(dict3)

#accessing dictionary
dict1={"key1":1,"key2":"value2",3:"value3"}
print(dict1.keys()) # all the keys are printed
dict1["key1"]="replace_one" # value assigned to key1 is replaced
print(dict1)
print(dict1["key2"])
dict1.values() # all the values are printed

#built-in methods
dict1={"fruit1":"apple","fruit2":"banana","veg1":"tomato"}
dict1.update({"veg2":"brinjal"})
print(dict1)
dict1.update({"veg3":"chilli"}) # updates the dictionary at the end
print(dict1)
dict1.pop("veg2")
print(dict1)

#searching method
dict1={"key1":"value1","key2":"value2"}
# dict1.index("key1") # will throw an error
print(dict1.get("key1"))