
'''In a oops, you can restrict access to methods and variables

    This can prevent the data from being modified by accident and is known as encapsulation

    Encapsulation can be achieved using private variables and private methods'''

''' public methods - accessible from anywhere
    private methods - accessible only in their own class starts with two underscores

    public variables - accessible from anywhere
    private variables - accessible only in their own class or by a method if defined starts with two underscores'''


''' private variable can be access only within the method '''

# class myclass:
#     __a=10
#     def display(self):
#         print(self.__a)
#
# obj=myclass()
# obj.display()
#
# print(myclass.__a) # error this is a private variable,we cannot access


''' private method can be access only within the method '''

# class myclass:
#     def __display1(self):  # private method
#         print('This is display1 method')
#
#     def display2(self):
#         print('This is display2 method')
#         self.__display1()
# #
# obj=myclass()
# obj.__diplay1() # not correct
# obj.display2()

''' we can access private variables outside of the class if class indirectly using methods '''

# class myclass:
#     __empid=101
#
#     def getempid(self,eid):
#         self.__empid=eid
#
#     def displayid(self):
#         print(self.__empid)
#
# obj=myclass()
#
# obj.getempid(102)
# obj.displayid()

