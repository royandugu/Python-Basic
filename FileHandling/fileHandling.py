#Just opening
file=open("myFile.txt","w+")
file.write("Hello world")
file.write("Hello world to be written twice")
things=file.read(100)
print(things)
file.close()