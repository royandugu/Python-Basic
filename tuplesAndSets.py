first_tuple=(1,"Royan")
print(first_tuple,type(first_tuple))

#Tuples don't support item assignment

#Creating sets
first_set={"Royan","Arshiya"}
print("Royan" in first_set)
first_set.add("Rohan")
print(first_set)
# del first_set #deleting basically means never defining it
# print(first_set) #returns error

#Adding something that already exists in sets
second_set={"Binesh","Layla"}
second_set.add("Binesh")
print(second_set)