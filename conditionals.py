i=0
if i>0:
    print("The number is positive")
elif i<0:
    print("The number is negative")
else:
    print("The number is zero")


##Nested conditionals
email,password="royan@yahoo.com","somethingfishy"
if email is None and password is None:
    print("Email and password not avaliable")
else:
    if email is None:
        print("Email is not avaliable")
    elif password is None:
        print("Password is not avaliable")
    else:
        print("Succesfully logged in")


#check if value is present in the list
ourList=[1,2,3,4]
x=8
if x in ourList:
    print(f"{x} is present in the list")
else:
    print(f"{x} is not present in the list")


if x not in ourList:
    print(f"{x} is not present in the list while checking for the second time")


#is
x=5
y=5
if x is y:
    print(f"{x} is {y}")
else:
    print(f"{x} is not {y}")