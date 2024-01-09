# Scope of Variables in Python
# The existence of a variable in a region is called its scope, or the accessibility of a variable defines it scope.

# Local Scope
# Whenever a variable is defined in a function, it can be used only in that function. The value of that variable cannot be accessed from outside the function. Let us see an example:
def demo():
    a = 100
    print(a)

demo()

# Global Scope
# A variable has Global Scope, if it’s created outside the function i.e. the code body and are accessible from anywhere. Let us see an example
a = 100

def demo():
    a = 150
    print(a)

print(a)

demo()

print(a)