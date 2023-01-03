# A variable is nothing but a reserved memory location to store values
# variables are used to store the data
# memory allocated when the values are stored in variables
# every variable must have some type

a=10
b=10.5
name='ritesh'
name1="mansi"
x=True

print(a)
print(b)
print(name)
print(name1)
print(x)

#multiple values to multiple variable
a,b,name=100,10.5,'ritesh'
print(a,b,name)

#same values to multiple variables
a,b,c=10,10,10
a=b=c=10
print(a,b,c)

###################################
x=1      #swap this two number
y=2

x,y=y,x #assign y value to the x and x value to the y
print(x,y)

import keyword
print(keyword.kwlist)
