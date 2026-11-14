# The programs define and gather some sort of data. That's way it helps to classify different types of data. The first data type we'll look at is the string. 

# A string is a series of characters. Anything inside quotes is considered a string in Python, and you can use single or double quotes around your strings like this: 

"This is a string"
"This is also a string"

'I told my friend, "Python is my favorite langauge!"' "The language 'Python' is named after Monty Python, not the snake." "One of Python's strengths is its diverse and supportive community"

# Changing Case in a String with Methods

import language_support_pkgs
name = "ada lovelace"
print(name.title())

# You can change a string to all uppercase or all lowercase letters like this. 

name = "Ada Lovelace"
print(name.upper())
print(name.lower())

# Using Variables as Strings 

# In some situations, you'll want to use a variable's value inside a string. 

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

# To insert a variable's value into a string, place the letter f immediately before the opening quotation mark. 

# These strings are called f-strings.  The f is for format. 

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")

# You can also use f-strings to compose a message, and then assign the entire message to a variable:

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)

# Adding Whitespace to Strings with Tabs or Newlines

#whitespaces refers to any nonprinting character, such as spaces, tabs, and end-of-line symbols. You can use whitespace to organize your output so it's easier for users to read. 

print("Python")

print("\tPython")

# To add a newline in a string, use the character combination \n

print("Languages:\nPython\nC\nJavaScript")

# You can also combine tabs and newlines in a single string. The string "\n\t" tells Python to move to a new line, and start the next line with a tab. 

print("Languages:\n\tPython\n\tC\n\tJavaScript")

# Python can look for extra whitespace on the right and left sides of a string. 

favorite_language = 'python '
favorite_language 

favorite_language.rstrip()

favorite_language





