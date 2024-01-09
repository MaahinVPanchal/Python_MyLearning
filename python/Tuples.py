# Python Tuples:-
# Tuple is a sequence in Python, a collection of objects. 
# Also, Python Tuples are immutable i.e. you cannot update a tuple or any of its elements. 
# Often, Lists and Tuples are confused in Python. 

# Creating Tuples
mytuple = (10,20,50,100)
print(mytuple)

# Accessing an element in tuple
print(mytuple[0])

# Empty Tuple
mytuple = ()
print(mytuple)

# The 'in' keyword is used to check existence of an item
mytuple = ("eddie","anthony","aran","blake","alyson","rechelle")
print("Tuple = ",mytuple)
print(mytuple[1:])
print(mytuple[::-1])

if "anthony" in mytuple:
    print("Found!")

mytuple1 = (20,40,80,150,200)
mytuple2 = (300,450,500)
print("Joining two tuples",mytuple1 + mytuple2)
print("The length of tuple-1",len(mytuple1))
print("The maximum of tuple-1",max(mytuple1))

# Convert List into Tuple
mylist = ["Messi","Neymar",3.5,50]
print("List = ",mylist)

mytuple3 = tuple(mylist)
print("Tuple = ",mytuple3)

# Delete items from Tuple
del mytuple3
print(mytuple3)