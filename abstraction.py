
''' Abstract classes are classes that contain one or more abstract methods

    An abstract method is a method that is declared, but contains no implementation

Abstract classed cannot be instantiated and require subclasses to provide implementation for the abstract methods

Subclasses of an abstract class in python are not required to implement abstract methods of the parent class'''

''' ABC is pre defined abstract class '''

from abc import ABC,abstractmethod

# class A(ABC):
#     @abstractmethod
#     def display(self):
#         None
#
# class B(A):
#     def display(self):
#         print('This is display method')
#
# b=B()
# b.display()


# from abc import ABC,abstractmethod
#
# class Animal(ABC):
#
#     @abstractmethod
#     def eat(self):
#         pass
#
# class Tiger(Animal):
#     def eat(self):
#         print('eat NON-VEG')
#
# class Cow(Animal):
#     def eat(self):
#         print('eat VEG')
#
# a=Tiger()
# a.eat()
#
# c=Cow()
# c.eat()

# from abc import ABC,abstractmethod
#
# class X(ABC):
#
#     @abstractmethod
#     def m1(self):
#         pass
#
#     @abstractmethod
#     def m2(self):
#         pass
#
# class Y(X):
#      def m1(self):
#         print('This is m1')
#
# class Z(Y):
#      def m2(self):
#         print('This is m2')
#
# z=Z()
# z.m1()
# z.m2()


# from abc import ABC,abstractmethod
#
# class cal(ABC):
#     def __init__(self,value):
#         self.value=value
#     @abstractmethod
#     def add(self):
#         pass
#     @abstractmethod
#     def sub(self):
#         pass
#
# class C(cal):
#     def add(self):
#         print(self.value+100)
#
#     def sub(self):
#         print(self.value-10)
#
# c=C(100)
# c.add()
# c.sub()






