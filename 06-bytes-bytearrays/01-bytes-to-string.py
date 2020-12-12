# create a string using the decode() method of bytes. 
#This method takes an encoding argument, such as UTF-8, and optionally an errors argument.
x = b'El ni\xc3\xb1o come camar\xc3\xb3n'
s = x.decode()
print(type(s))
print(s)