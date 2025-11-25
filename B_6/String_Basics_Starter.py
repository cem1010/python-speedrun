
first = "Nico"
last = "Hulkenberg"

# - Create a variable called "full_name" that combines first and last with a space between them.  
# - Print it out

print(first+" "+last)

def add(a,b):
    return a+b
a=0
a=add(3,2)
print(a)

# - Create an "initials" variable that holds the first character of first followed by the first character of last. 
# - Print it out
def initials(firstname,lastname):
    return firstname[0:1]+lastname[0:1]
a=initials(first,last)
print(a)


# - Create an "initials_2" variable that holds the first character of first followed by the first character of last, with periods after each letter!
# - Print it out
def initials(firstname,lastname):
    return firstname[0:1]+"."+lastname[0:1]+"."
a=initials(first,last)
print(a)


# Create a "nickname" variable that holds the first 4 characters of "last" (use a slice)
# Print it out 
def nickname(lastname):
    return lastname[0:5]
a=nickname(last)
print(a)
