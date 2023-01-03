# A function is a block of code which only runs when it is called
# you can pass data,known as parameters into a function
# A function can return data as a result

# re-usable pieces of code which help us to organize structure of the code
# we create functions so that we can run a set of statements
# multiple times during in the program without repeating ourselves

# def myfun():
#     pass
#
# myfun()

# def sum(start,end):
#     result=0
#     for i in range(start,end+1):
#         result+=i
#     print(result)
# sum(1,5)
# sum(10,20)


# def sum(start,end):
#     result=0
#     for i in range(start,end+1):
#         result+=i
#     return result
# s=sum(1,5)
# a=sum(10,20)
# print(s)
# print(a)


# def sum(start,end):
#     if start>end:
#         print('start should be less than end')
#         return
#     result=0
#     for i in range(start,end+1):
#         result=result+i
#     return result
# a=sum(1,5)
# print(a)


# def test():
#     i=100
#
# print(test())


'''global variables: variables that are not bound to any function,
                     but can be accessed inside as well as outside the function

local variables: variables which are declared inside a function'''


# global_var=12
#
# def fun():
#     local_var=100
#     print(global_var)
# fun()
#
# print(global_var)
# print(local_var)

# xy=100
#
# def cool():
#     xy=200
#     print(xy)
# cool()
#
# print(xy)

# t=1
#
# def increment():
#     global t
#     t=100
#     print(t)
#
# increment()
#
# print(t)

'''argument with default values(positional)'''

# def fun(i,j=100):
#     print(i,j)
#
# fun(50)
# fun(50,250)

'''keyword arguments'''

# def name_args(name,greeting):
#     print(greeting +' '+name)
#
# name_args('pavan','Hi') # positional arguments
#
# name_args(name='pavan',greeting='Hi') # keyword arguments


# def myfun(a,b,c):
#     print(a,b,c)
#
# myfun(10,20,30)  # positional arguments
#
# myfun(10,b=20,c=30)  # positional & keyword arguments
#
# myfun(12,b=20,30) # incorrect


'''returning multiple values from function
   we can return multiple values from function 
   using the return statement by separating them with (,)
   multiple values are returned as tuples'''


# def bigger(a,b):
#     if a>b:
#         return a,b
#     else:
#         return b,a
#
# s=bigger(100,200)
# print(s)
#
# print(type(s))
