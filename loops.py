#Using loops

#for loop
ourList=[1,2,3,5,4]
for item in ourList:
    print(f"{item} is our item")
#break demo eutai nai ho
for item in ourList:
    if item==5:
        break
    print(f"{item} is our item")


i=0
for i in range(5):
    print(f"{i} is our 3rd item")
    i=i+1

#For range
j=0
for j in range(0,11):
    print(f"{j} is our 4th item")
    j=j+1

#while
k=0
while k<11:
    print(f"{k} is our 5th item")
    k=k+1