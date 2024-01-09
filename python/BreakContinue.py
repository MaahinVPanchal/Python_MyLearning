# Python break and continue statements
# The break and continue statements are called Decision-Making Statements

# break statement in Python
# In the break statement, the current loop is terminated and the execution of the program is aborted. After termination, the control reaches the next line after the loop.

mystr = "Maahin"
print("String = ",mystr)
for i in mystr:
    if i == 'i':
        break;
    print(i)

# continue statement in Python
# The continue statement in Python transfers control to the conditional expression and jumps to the next iteration of the loop.

mystr = "Maahin"
print("String = ",mystr)
for i in mystr:
    if i == 'i':
        continue;
    print(i)