#
#
#
#

name,number=("Hello world",12)
print(name)
print(type(name))
del name
# print(name) Throws an error anyway

name="Royan dugu"
firstname,lastname=name.split(" ") #This logic can be used for tokens
print(firstname)
print(lastname)