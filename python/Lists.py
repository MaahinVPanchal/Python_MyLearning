# Python List:-
# Lists in Python are ordered. It is modifiable and changeable, unlike Tuples. Tuples in Python are immutable, whereas Lists are mutable. In other words, the Lists can be modified even after it’s created.
# Example of List:-

mylist = ["Meet","Maan","Harsh","Rudra"]

# Accessing List
mylist[2]

# Removing elements from List
del mylist(3)

# Remove element from a specific position (index) in the List
del mylist[3]

# Remove a specific element from a Python List
mylist.remove("Rudra")

# Delete the entire List
del mylist

# Remove multiple elements from a List
del mylist[2:4] # Above, we deleted elements from 2 (including) to 4 (excluding) indexes. 
                # Therefore, we deleted two elements i.e. index 2 and index 3.

# Add elements to the List
mylist.append("Sam")

# Add element at a specific index in List
mylist.insert(2,"Pashwa")

# Check if a specific item exists in a List
if "Rudra" in mylist:
    print("Found")

# Extend the List by adding another List to the end
mylist1 = ["Dhruv","Devansh","Neel"]
mylist.extend(mylist1)

# Length of list
print("The length of list = ",len(mylist))

# Max and Min Value from List
mylist2 = [12,-2,45,666,0]
print("The maximum value of List = ",max(mylist2))
print("The minimum value of List = ",min(mylist2))

# Making a Copy 
mylist3 = mylist2.copy()
print(mylist3)

# Join and Concancate
mylist4 = mylist3 + mylist2
print(mylist4)

# Sort List
mylist.sort()
print("The sorted list = ")
for v in mylist:
    print(v)

# Reverse List
mylist.reverse()
print("The reverse list = ")
for v in mylist:
    print(v)

# Multidimensional
mylist5 = [[10,20,30,40],[50,60],[80],[90,100,200]]
print(mylist5)