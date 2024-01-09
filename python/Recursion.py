# Recursion in Python :--
# When a function calls itself, it is called Recursion.  
# In another sense, with Recursion, a defined function can call itself. 
# Recursion is a programming approach, which makes code efficient and reduces LOC. 
 
# Factorial example:-

def fact(num):
    if(num == 0):
        return 1
    else:
        return num * fact(num-1)
print("0! = ",fact(0))
print("1! = ",fact(1))
print("7! = ",fact(7))
print("10! = ",fact(10))