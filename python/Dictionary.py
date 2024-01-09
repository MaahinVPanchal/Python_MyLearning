# Python Dictionary:-
# Dictionary represents the key-value pair in Python, enclosed in curly braces. 
# Keys are unique and a colon separates it from value, whereas comma separates the items. 
# The keys are immutable (strings, numbers, etc.), whereas the value can be of any Python object. 
# Apart from this, Keys in Dictionary are case-sensitive.

# Note: You can easily relate Python Dictionaries with the real-world Dictionary, such as a word with its meaning as key-value pair.

mystock = {
    "Product" : "Earphone",
    "Price" : 800,
    "Quantity" : 50 
}
print(mystock)

# Dictionary using the dict() method:
mystock = dict ({
    "Product" : "Earphone",
    "Price" : 800,
    "Quantity" : 50 
})

# Empty Dictionary
newstock = {}

# Accessing values from Dictionary
print(mystock["Product"])

print("Keys = ",mystock.keys())  # Accessing Keys

print("Keys = ",mystock.values())  # Accessing Values

mystock["Price"] = 1800 # Updating
print("Keys = ",mystock.values())

mystock["Rating"] = 5 # Adding 
print("Keys = ",mystock.values())

del mystock['Price'] # Delete an element in a Dictionary with a specific key
print("Keys = ",mystock.values())

# Delete a key and return the corresponding value
result = mystock.pop("Product")
print("Corresponding value with poped key Quantity = ",str(result))

# Iterate through a Dictionary
for p in mystock:
    print(mystock[p])
    
# Equivalent String
print ("String = %s" % str (mystock))

# Calculate length
print("Updated Length = ",len(mystock))

# Copy of Dictionary
mystock2 = mystock.copy()

# Creating multidimensional Dictionary
products = {1:mystock,2:mystock2}

# mystock.clear() # Emptying the Dictionary

# del mystock # Complete Dictionary is deleted.

# Properties of Dictionary keys
# Following defines what Dictionary keys rules are:

    # Keys are unique and cannot be repeated.
    # Dictionary Keys are case-sensitive.
    # Keys are immutable.
    # Key can be a number, tuple or string.

# Creating Nested Dictionary
products = {
  "mystock1" : {
   "Product": "SSD",
   "Price": 3000,
   "Quantity": 100,
   "InStock" : "Yes"
  },
  "mystock2" : {
   "Product": "HDD",
   "Price": 2500,
   "Quantity": 50,
   "InStock" : "Yes"
  },
  "mystock3" : {
   "Product": "Headphone",
   "Price": 2800,
   "Quantity": 40,
   "InStock" : "Yes"
  },
  "mystock4" : {
   "Product": "Earphone",
   "Price": 1500,
   "Quantity": 10,
   "InStock" : "No"
  }
}
 
#Printing the Nested Dictionary
print("Nested Dictionary = ",products)

#Accessing element from Nested Dictionary
print(products["mystock1"]["Product"])