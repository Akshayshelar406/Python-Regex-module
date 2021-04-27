import re

s = "hello from python"

#Check if the string ends with 'world':

i = re.findall("on$", s)

if (i):
    print("String Match")
else:
    print("No match")