
'''classes can inherit functionality of other classes
   if an object is created using a class that inherits from a superclass
   the object will contain the methods of both the class and superclass
   the same holds true for variables of both the superclass and the class that inherits from the super class'''


''' Single inheritance(1 parent 1 child class) '''

# class A:
#     def m1(self):
#         print('This is m1 method from class A')
#
# class B(A):
#     def m2(self):
#         print('This is m2 method from class B')
#
# a=A()
# a.m1()
#
# b=B()
# b.m1()
# b.m2()

# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
#
# class B(A):
#     a,b=100,200
#     def m2(self):
#         print(self.a+self.b)
#
#
# b=B()
# b.m1()
# b.m2()

''' Multilevel inheritance(A is parent of B, B is a parent of c) '''

# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
#
# class B(A):
#     a,b=100,200
#     def m2(self):
#         print(self.a+self.b)
#
# class C(B):
#     i,j=1,2
#     def m3(self):
#         print(self.i+self.j)
#
# b=B()
# b.m1() #A
# b.m2() #B
#
# c=C()
# c.m1() #A
# c.m2() #B
# c.m3() #C

''' Hierarchical inheritance( 1 parent class for multiple child class) '''

# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
#
# class B(A):
#     a,b=100,200
#     def m2(self):
#         print(self.a+self.b)
#
# class C(A):
#     i,j=1,2
#     def m3(self):
#         print(self.i+self.j)
#
# b=B()
# b.m1()
# b.m2()
#
# c=C()
# c.m1()
# c.m3()


''' Multiple inheritance(2 parent class and one child class) '''

# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
#
# class B:
#     a,b=100,200
#     def m2(self):
#         print(self.a+self.b)
#
# class C(A,B):
#     i,j=1,2
#     def m3(self):
#         print(self.i+self.j)
# c=C()
# c.m1()
# c.m2()
# c.m3()

''' Supar() '''

''' supar() can be used in 3 ways
            to invoke parent class methods
            to invoke parent class variables
            to invoke parent class constructor '''

# class A:
#     def m1(self):
#         print('This is method from A')
#
# class B(A):
#     def m2(self):
#         print('This is method from B')
#         super().m1()  # calling parent class method using super()
# b=B()
# b.m2()


# class A:
#     a,b=10,20
#
# class B(A):
#     i,j=100,200
#     def m1(self,x,y):
#         print(x+y) # local variables
#         print(self.i+self.j)  #child class variables
#         print(self.a+self.b)  #parent class variables
#
# b=B()
# b.m1(1,2)


# a,b=15,20
#
# class A:
#     a,b=10,20
#
# class B(A):
#     a,b=100,200
#     def m1(self,a,b):
#         print(a+b) # local variables
#         print(self.a+self.b)  #child class variables
#         print(super().a+super().b) #parent class variables
#         print(globals()['a'] + globals()['b'])  # global variables
# bOBJ=B()
# bOBJ.m1(1,2)


# class A:
#     def __init__(self):
#         print('constructor from class A')
#
# class B(A):
#     pass
#
# bobj=B()


# class A:
#     def __init__(self):
#         print('constructor from class A')
#
# class B(A):
#     def __init__(self):
#         print('constructor from class B')
#         super().__init__()    # approach 1
#         A.__init__(self)      # approach 2
# #
# bobj=B()

