'''class is a logical entity which contains logic
    class contains variables and methods
   logic should be included within a method

   Object is physical entity which is created for a class
   We can create any number of object for a class

   class is a blue-print of object'''

'''Creating basic class and object which include methods'''

# class myclass:
#
#     def myfun(self):
#         pass
#     def display(self,name):
#         print('Name is:',name)
#
# a=myclass()
# a.myfun()
# a.display('scott')

'''Instance method and static method'''

# class myclass:
#     def m1(self):
#         print('Instance method')
#
#     @staticmethod
#     def m2():
#         print('Static method')
#
# a=myclass()
# a.m1()
# a.m2()
#
# myclass.m2()  #we can call the static method using class name


'''Declaring variables inside the class'''

# class myclass:
#     a,b=100,200  # class variables
#
#     def add(self):
#         print(self.a + self.b)
#     def mul(self):
#         print(self.a*self.b)
#
# a=myclass()
#
# a.add()
# a.mul()


'''local,global,class variables'''
#
# i,j=15,25  # global variables
#
# class myclass:
#     a,b=10,20   # class variables
#
#     def add(self,x,y):   # local variables
#         print(x+y)     # accessing local variables
#         print(self.a+self.b)   #accessing class variables
#         print(i+j)   # accessing global variables
#
# a=myclass()
# a.add(100,200)


'''global variables,class variables,local variables with same name'''

# a,b=15,25  # global variables
#
# class myclass:
#     a,b=10,20   # class variables
#
#     def add(self,a,b):   # local variables
#         print(a+b)     # accessing local variables
#         print(self.a+self.b)   #accessing class variables
#         print(globals()['a']+globals()['b'])   # accessing global variables
#
# x=myclass()
# x.add(100,200)


'''creating multiple object for one class'''

# class myclass:
#     def display(self):
#         print('Good morning')
# obj1=myclass()
# obj1.display()
#
# obj2=myclass()
# obj2.display()


'''checking memory location of object'''

# class myclass:
#     def m1(self):
#         pass
#
# c1=myclass()
# c2=myclass()
# c3=c1
#
# print(id(c1))
# print(id(c2))
# print(id(c3))
#
# print(c1 is c2)
# print(c1 is c3)
# print(c1 is not c2)
