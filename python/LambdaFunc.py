# Python Lambda Functions:-
# A lambda function is a function without a name i.e. an anonymous function. 
# The keyword lambda is used to define a lambda function in Python and has only a single expression.

# Syntax of Lambda Functions:-
# lambda arguments: expressions
# The lambda function can have any number of arguments, but only one expression.

# Multiplying a number to an argument.
val = lambda i: i*2
print("Result = ",val(25))

# Display a string.
str = "Hello World!!!"
(lambda str : print(str))(str)

# More than Arguments
val = lambda i,j,k : i*j*k
print("Result = ",val(10,20,30))

# Maximum of two numbers
res = lambda i,j : i if(i>j) else j
print("Maximum = ",res(50,100))

# Square of a numbers
val = lambda i : i*i
print("Result = ",val(9))