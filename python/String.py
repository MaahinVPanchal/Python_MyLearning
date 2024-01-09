# str.capitalize() -- only for first letter of string
# str.casefold() -- used to convert a string into lowercase
# str.center() -- align a string centrally
    # string.center(len, char)
    # Above, len is the length of the string, whereas, char is the character to filled on left and right side.
    # str.center(10,"#")
# str.count(str, begn, end) -- used to search for a specific value and its count of appearance in string
# str.encode() -- encodes the string . Default is UTF - 8
# str.find() -- search for a specific letter in a string.
    # str.find(str, begn, end)
# str.endswith() -- The endswith() method in Python is used to check for a string. If this string ends with the specified value, TRUE is returned, else False.
    # str.endswith(str, begn, end)
# str.expandtabs() -- used to set the tab size. Default tab size = 8
# str.index(str,begin,end) -- find the index of the first occurrence of a specific value.
# str.isalnum() -- The isalnum() method in Python returns TRUE, if all the characters in the string are alphanumeric, else FALSE is returned.
# str.isalpha() -- The isalpha() method in Python returns TRUE, if all the characters in the string are alphabet, else FALSE is returned.
# str.isdecimal() -- The isdecimal() method in Python returns TRUE, if all the characters in the string are decimals, else FALSE is returned.
# str.isdigit() -- The isdigit() method in Python returns TRUE, if all characters in the string are digits, else FALSE is returned.
# str.isidentifier() -- The isidentifier() method in Python returns TRUE, if the string is an identifier, else FALSE is returned.
    # Note: Valid identifier doesn’t begin with a number. It doesn’t even include spaces. 
    # However, a string is a valid identifier, if it includes (a-z), (0-9), or (_).
# str.islower() -- The islower() method in Python returns TRUE, if all the characters in the string are lowercase, else FALSE is returned.
# str.isnumeric() -- The isnumeric() method in Python returns TRUE, if all the characters in the string are numeric, else FALSE is returned.
# str.isprintable() -- The isprintable() method in Python returns TRUE, if all the characters in the string are alphabet, else FALSE is returned.
# str.isspace() -- The isspace() method in Python returns TRUE, if all the characters in the string are whitespaces, else FALSE is returned
# str.istitle() -- The istitle() method in Python returns TRUE, if all the string considers the rules of a title (i.e. uppercase title), else FALSE is returned. Uppercase titles, example, “Demo Text”, “Mark”, etc.
# str.isupper() -- The isupper() method in Python returns TRUE, if all the characters in the string are uppercase, else FALSE is returned.
# str.join() -- The join() method in Python join is used to join the iterable elements to the end of the string. Containers, such as Tuple, String, Dictionary, etc. are iterables in Python.
# str.lower() -- The lower() method in Python is used to convert the uppercase letters in the string to lowercase.
# str.lstrip() -- The lstrip() method in Python is used to remove characters from the left of the string. Default is whitespace. 
# str.replace(old,new,count) -- The replace() method in Python is used to replace a value with another.
# str.rfind(val,begin,end) -- The rfind() method in Python is used to find the last occurrence of a value from a string.
# str.rindex(val,begin,end) -- The rindex() method in Python is used to get the index of the last occurrence of a specific value.
        # Note: rindex() is the same as rfind().
# str.rjust(len,chars) -- The rjust() method in Python is used to right align the string and fill characters to the left.
        # Above, len is the total length of the string to be returned, whereas chars are the characters to be filled on the left.
# str.rsplit(sep,split) -- The rsplit() method in Python is used to split a string, beginning from the right. A list is returned.
        # Above, sep is the separator used while splitting, and split is the number of splits to be performed. If you won’t mention anything, that would mean “all occurrences”.
# str.rstrip(ch) -- The rstrip() method in Python is used to remove characters from the right of the string. Default is whitespace.
# str.split(sep,split) -- The split() method in Python is used to split a string into a list. You can also set the separator. Whitespace is the default separator.
        # Above, sep is the separator used while splitting, and split is the number of splits to be performed. If you won’t mention anything, that would mean “all occurrences”.
# str.splitlines(linebrk) -- The splitlines() method in Python is used to split a string into list. You can also set option to allow line breaks or not.
        # Above, linebrk is a boolean value to set whether to allow line breaks or not.
str = "One\nTwo\nThree\nFour"
res = str.splitlines(False)
print("Result = ",res)

# str.startswith(val,begin,end) -- The startswith() method in Python returns TRUE, if string begins with a particular value., else FALSE is returned.
        # Above, val is the value to be checked where the string begins with, begin is the position where the search begins, and end is the position where the search ends.
# str.swapcase() -- The swapcase() method in Python is used swap the case i.e. convert lowercase to uppercase, and vice versa.
# str.title() -- The title() method in Python is used to convert the first letter of every work lettercase i.e. title, heading, etc.
# str.upper() -- Use the upper() method in Python to convert the lowercase letters in the string to uppercase.
# str.zfill(len) -- The zfill() method in Python is use to fill zeros in the beginning of the string.
        # Above, the parameter len is the total length of the string including the zero fill.
# str.strip(ch) -- The strip() method in Python is used to remove spaces from the beginning and end of a string.
        # Above, the parameter ch are the set of characters to be removed from the beginning and end of the string.