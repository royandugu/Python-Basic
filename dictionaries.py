person={
    "name":"Royan",
    "age":20
}
print(person, type(person))
print(person["name"])
#Dictionaries are key-value pairs like object literals in JS

person["phone"]=8888
#add a keyvalue pair
print(person)
print(person.keys())

del person["phone"]
#We can also remove the age but this time we get the age value

age=person.pop("age")
print(person)
print(age)


#List of dictionaries
people=[
    {"name":"Royan",age:10},
    {"name":"Arshiya",age:20}
]
print(people[0]["name"])