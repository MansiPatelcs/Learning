
'''formatting data with the % & {}'''

# %d int
# %s string
# %f or %g float

name="zohn"
age=25
sal=10000.25

#approach 1
print(name,age,sal)

#approach 2
print('Name is', name)
print('Age is', age)
print('Salary is', sal)

#approach 3  using % operator  here type is imp
print('Name:%s Age:%d Salary:%g'%(name,age,sal))

#approach 4
print('Name:{} Age:{} Salary:{}'.format(name,age,sal))

#approach 5
print('Name:{0} Age:{1} Salary:{2}'.format(name,age,sal))




