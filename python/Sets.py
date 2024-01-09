# Python Sets:-
# A Python Set is a Collection. Collections in Python include the following: List, Sets, Dictionary and Tuple.

# A Set is a collection in Python
# Set items i.e. elements are placed inside curly braces {}
# Unordered and Unchangeable
# Unchangeable, but you can add/ remove an item
# Duplicate values aren’t allowed in a Set.

myset = {"maahin","dhruv","dev","ali","chirag"}
for i in myset:
    print(i)
print("The length = ",len(myset))

# Accessing items in Sets
print("maahin" in myset)

# Add an item to Set
myset.add("zakir")
print(myset)

# Add items from another set into the current set
myset1 = {"fuzail","sujal","abhay","hardik"}
myset.update(myset1)
print(myset)

# Remove an item from the Set using remove()
myset.remove("dhruv")
print(myset)

# Remove an item from the Set using discard()
myset.discard("ali")
print(myset)

# Empty the Set
myset1.clear()
print(myset1)

# Delete the complete Set
# del myset1

# Return the Difference between two or more sets
setA = {12,10,30,5,4}
setB = {1,2,5,4,10}
print(setA)
print(setB)
result = setA.difference(setB)
print("The difference between two set = ",result)

# Keep only the duplicate items in two sets
setA.intersection_update(setB)
print("The intersection_update two set = ",setA)
setA.symmetric_difference_update(setB)
print("Keep all the items in the two sets except the duplicates = ",setA)
mysetA = myset.copy()
print(mysetA)
result2 = setA.union(setB)
print("Union of two set = ",result2)