
''' Modules ia a python file(.py) containing a set of functions you want to include in your application

    A module's contents are accessed with the import statement'''

'''Approach 1'''

# import operation
#
# operation.add(10,20)
# operation.mul(10,20)


'''Approach 2'''

# from operation import add,mul
#
# add(10,20)
# mul(10,20)


'''Approach 3'''

# from operation import *
#
# add(10,20)
# mul(10,20)


'''Approach 1'''

# import animal
# import Bird
#
# animal.fly()
# animal.color()
#
# Bird.fly()
# Bird.color()


'''Approach 2'''
#
# from animal import *
#
# fly()
# color()
#
# from Bird import *
#
# fly()
# color()


'''Approach 1'''

# import A
# import B
#
# obj=A.animal()
# obj.display()
#
# obj2=B.bird()
# obj2.display()

'''Approach 2'''

# from A import animal
# from B import bird
#
# obj=animal()
# obj.display()
#
# obj2=bird()
# obj2.display()


# import m
#
# print(dir(m))  # dir function returns how many classes are created
#
# import animal
#
# print(dir(animal))  # dir function returns how many function are created inside the module
