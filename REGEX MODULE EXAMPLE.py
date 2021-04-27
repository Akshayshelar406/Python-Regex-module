import re

i = "Hello from Python"

#Find all lower case characters alphabetically between "a"and "m":

x = re.findall("[a-z]", i)

print(x)