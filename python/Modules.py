# Python Modules:-
# The modules in Python are used to organize the code. 
# We can easily import a module in Python using the import statement. 
# A module can be considered as a file with a code. 
# This module can easily define functions and classes

# To load a module in Python, use,

# import statement
# from-import statement

# import statement:--
# To import a module in Python, use the import statement,
# import module1,module2, module3 ... module n
 
    # Example:
    # import math
 
# from-import statement:--
# To import only the specific attributes of a module, use the from-import statement,

    # Example:
    # from os import path
    
# Math module:--
print("Math module")
import math as m 
print(m.sqrt(36))
print(m.log(4))
print(m.ceil(-5.55))
print(m.floor(25.99))
print(m.pow(2,7))
print(m.fabs(-98.00))# returns absolute value
print(m.factorial(7))
print(m.sin(90))
print(m.sin(m.degrees(30)))
print(m.cos(30))
print(m.cos(m.radians(30)))
print(m.tan(30))
print(m.tan(m.radians(30)))
print("----------------------------------")
# Statistics module 
print("Statistics module")
import statistics as st

print(st.mean([10,20,30,40,50,60]))
print(st.median([5,10,-3,98,65]))
print(st.mode([1,3,3,4,4,5,4,3,3]))
print(st.stdev([1,5,9,100,34]))
print("---------------------------------------")

print("Random module")
import random as rm

print(rm.random())
print(rm.randint(5,10))
mylist = ["John","Amit","Mark"]
print(mylist)
print(rm.choice(mylist))
print(rm.randrange(3,10))