# Functions in Python with Examples
# A function in Python is an organized block of reusable code, which avoid repeating the tasks again and again. If you want to do a task repeatedly in a code, then just make a function, set the task in it and call the function multiple times whenever you need it. Functions in Python begins with the keyword def and is followed by the name of the function and parentheses.

# Create a function in Python
# Functions in Python, use the def keyword as in the below syntax:

# def function_name( parameters ):
#     function_suite
#     return [expression]
 
# Above,
# The def keyword is used to define a function name,
# The parameters are optional to add,
# To return a value, the return statement is used.

def demo():
    print("We provide free tutorials and interview questions");
    print("We also provide interview questions and answers");
    
demo()

# Function Parameters
# The names entered in the function at the time of defining it, are Function Parameters. Adding Parameters to a function in Python is optional.

def demo1(str):
    print("The name is : ",str)

demo1("Maahin")

# Function Arguments in Python
# In Python,

# Required arguments:-
    # The required arguments as the name suggests are the required number of arguments to be passed on a function call. 
    # When you call a function, the arguments in the call are to match with the function definition for the program to run correctly. 
    # An error occurs even if the position of the argument is changed.

def area(l,b):
    print("Area of Rectangle = ",l*b)
area(10,20)

# Keyword arguments:-
    # Call a function with keyword arguments in Python. 
    # Through this, you can skip arguments or even pass them in any order while calling a function. 
    # As we saw above, this is definitely different that Required arguments wherein the order in which the arguments are passed is the same while calling.

def details(name,rank):
    print("Student Name = ",name)
    print("Student rank = ",rank)
details(rank = 5,name="jack")

# Arbitrary Keyword Arguments:-
    # Add two asterisks ** before the parameter name in a function definition, if you don’t know in advance how many keyword arguments will be passed to your function. 
    # A dictionary format gets created for such arguments i.e. a Dictionary of arguments.

def demo1(**stu):
    print("STUDENT NAME: " +stu["STUDENT"])
    print("STUDENT SECTION: " +stu["SECTION"])
demo1(STUDENT = "Jack", SECTION = "AD")

# Default arguments:-
    # While calling a function, if the value isn’t passed, a default value is assumed for that argument.

def details1(name, rank=10):
    print("---------------------------")
    print("student Name = ",name)
    print("student Rank = ",rank)
    print("---------------------------")
details1(name = "John",rank = 5)
details1(name = "Mark",rank = 8)
details1(name = "Jacob")

# Variable-length/ Arbitrary arguments:-
# Arbitrary arguments work when you have no idea about the number of arguments to be passed. 
    # These are variable length arguments, allowing you to pass any number of arguments, defined as * (asterisk). 
    # That means, include a * before the parameter name while defining the function.

def demo(*sports):
    print("Sports 1 = ",sports[0])
    print("Sports 2 = ",sports[1])
    print("Sports 3 = ",sports[2])
demo("Football","Hockey","Cricket")