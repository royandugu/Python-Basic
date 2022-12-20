#My first function in python
def printText(text):
    print(text)

printText("Hello world")

i=1
#recursion loop
def oneToFive(i):
    if i==6:
        return
    print(i)
    oneToFive(i+1)

oneToFive(i)

#Hello name
def sayHello(name):
    print(f'Hello {name}')
    
sayHello("Royan")


#without using a Lamda
def getSum(num1,num2):
    return num1+num2
print(getSum(2,1))

#using a lambda
getSumLam=lambda num1,num2 : num1+num2 #lambda function that returns the sum of two numbers
print(getSumLam(2,1))