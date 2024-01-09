# Python File Handling
# In Python, we can easily create, read, and operate on files. 
# Python provides methods for creating and reading a new file, reading only specific parts of a file, writing data to an already created file, updating, deleting a file, etc.

# file = open("demo.txt")

# Create
# file = open("demo.txt","x")

# Append
# file = open("demo.txt","a")

# Write
# file = open("demo.txt","w")

# Read a file
file = open("E:\\Python-Programming\python\FileHandlingdemo.txt","r")
print("Reading the contents of the file...\n",file.read())

# Read some content (characters)
file = open("E:\\Python-Programming\python\FileHandlingdemo.txt","r")
print("Reading the contents of the file...\n",file.read(10))

# Read specific lines
file = open("E:\\Python-Programming\python\FileHandlingdemo.txt","r")
print("Reading only two lines of the file...\n",file.readline())

file = open("E:\\Python-Programming\python\FileHandlingdemo.txt","w")
file.write("We have overwritten the existing content with this line!")
file.close()