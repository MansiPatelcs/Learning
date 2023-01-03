
''' *args allow us to pass variable number of arguments to the function'''

# def sum(a,b):
#     print('sum is', a+b)

'''This program only accepts two numbers, what if you want to pass more than two arguments, this is where
   *args comes into play'''

# def sum(*args):   # '*' representing multiple values
#     s=0
#     for i in args:
#         s=s+i
#     print('sum is', s)
# sum(1,2)
# sum(1,2,3)
# sum(10,20,30,40)

# def my_three(a,b,c):
#     print(a,b,c)
#
# args=[1,2,3]
# my_three(*args)


''' **kwargs allow us to pass variables number of keyword argument like this'''


# def fun(a,b,c):
#     print(a,b,c)
#
# a={'a':'one', 'b':'two', 'c':'three'}
#
# fun(**a)

# def fun(**kargs):
#     for i,j in kargs.items():
#         print(i,j)
#
# fun(name='tom', spot='football', roll=10, height=5)
