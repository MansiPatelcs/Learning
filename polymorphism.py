
'''sometimes an object comes in many types or forms

 if we have a button,there are many different draw outputs(round button, check button, square button,

 button with image) but they do share the same logic:onclick()

 we access them using the same method. This idea is called polymorphism'''


''' method overriding '''


'''Overriding means having two methods with same name but doing different tasks

   it means that one of the methods overrides the other

   if there is any method in the superclass and a method with the same name in a subclass,
   then by executing the method of the corresponding class will be executed'''

''' Overrding a variable '''

# class parent:
#     name='scott'
#
# class child(parent):
#     name='david'
#
# obj=child()
# print(obj.name)


''' Overriding methods '''

# class bank:
#     def rateofinterest(self):
#         return 0
# class ICIC(bank):
#     def rateofinterest(self):
#         return 10.5
#
# obj=ICIC ()
# print(obj.rateofinterest())
#
# obj1=bank()
# print(obj1.rateofinterest())


''' Method overloading '''

'''In python you can define a method in such a way that there are multiple ways to call it
   given a single method or function, we can specify the number of parameters our self '''

# class Human:
#     def sayhello(self,name=None):
#         if name is not None:
#             print('Hello '+ name)
#         else:
#             print('Hello')
#
# obj=Human()
# obj.sayhello()
# obj.sayhello('scott')

# class bird:
#     def fly(self,name=None):
#         if name=='parrot':
#             print('can fly')
#         if name=='penguine':
#             print('cannot fly')
#         if name is None:
#             print('NO input')
#
# obj=bird()
# obj.fly()
# obj.fly('parrot')
# obj.fly('penguine')

