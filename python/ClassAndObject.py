# Python Classes and Objects:-
# Python is an interpreted high-level, structural, and object-oriented programming language. 
# Since it is object-oriented, the concept of classes and objects is well-discussed and implemented. 
# A class is the basis of object-oriented programming in Python. 
# In this tutorial, we will learn about Classes and Objects in Python. 
# A class is a template for an object, whereas an object is an instance of a class.

class Bike:
    
    # attributes of Bike
    name = "Royal Enefield"
    body = "GEN III"
    engine = 1340

    # Custom Python function
    def demoFunc(self):
        print("\nBike = ",self.name)
        print("Body = ",self.body)
        print("Engine (cc) = ",self.engine)

# Objects
b1 = Bike()
b2 = Bike()

# Accessing using the 1st object
print("Bike name = ",b1.name)
print("Bike Engine = ",b1.engine)

# Calling using the 2nd object
b2.demoFunc()

# Python _init_() Function:-
# The classes in Python have __init__() function. 
# Like constructors in Java, the __init__() function executes when the object gets created. 
# Using this method, easily assign values to object properties.

class Students:
    
    # using the __init__ function
    def __init__(self, sname, ssub, sgrade):
        self.sname = sname
        self.ssub = ssub
        self.sgrade = sgrade
        
    def demofunc1(self):
        print("I am " +self.sname)
        print("I am interested in the Subject "+self.ssub)
        
st1 = Students("Maahin", "Data Analytics","A+")
st2 = Students("Mark", "DBMS","B+")
st3 = Students("Jack", "Operating System","O+")

st1.demofunc1()
st2.demofunc1()
st3.demofunc1()