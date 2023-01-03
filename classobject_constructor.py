# class myclass:
#     def n1(self):        # method contains logic
#         print('Good morning')
#     def __init__(self):    # constructor contains initialization
#         print('This is constructor')
#
# c=myclass()
# c.n1()


'''converting local variables to class variables'''

# class myclass:
#     def values(self,val1,val2):  # val1 and val2 are local variables
#         print(val1)  #local variables
#         print(val2)  #local variables
#         self.val1=val1
#         self.val2=val2
#
#     def add(self):
#         print(self.val1+self.val2)  # class variables
#
# a=myclass()
# a.values(10,20)
# a.add()

# class myclass:
#     def __init__ (self,val1,val2):  # val1 and val2 are local variables
#          print(val1)
#          print(val2)
#          self.val1=val1
#          self.val2=val2
#
#     def add(self):
#          print(self.val1+self.val2)
#
# a=myclass(100,200)
# a.add()

'''How to call current class method in another method'''

# class myclass:
#     def n1(self):
#         print('this is n1 method')
#         self.n2(100)
#
#     def n2(self,a):
#         print('this is n2 method',a)
#
# c=myclass()
# c.n1()

'''constructor with arguments'''

# class myclass:
#     name='patel'
#     def __init__(self,name):
#         print(name)  #constructor argument local
#         print(self.name)   #represents class variables
#
# c=myclass('mansi')


# class emp:
#     def __init__(self,eid,ename,sal):
#         self.eid=eid
#         self.ename=ename
#         self.sal=sal
#
#     def display(self):
#         print('EmpId:{} EmpName:{} EmpSal:{}'.format(self.eid,self.ename,self.sal))
#         print('EmiId:%d EmpName:%s EmpSal:%g' %(self.eid,self.ename,self.sal))
#
# e1=emp(101,'smith',10000)
# e1.display()

''' __str__  executes automatically when you print referance variables'''

# class myclass:
#     pass
# a=myclass()  # a is the reference variable
# print(a)

#
# class myclass:
#     def __str__(self):
#         return 'welcome'
#
# a=myclass()  # a is the reference variable
# print(a)


# class emp:
#     def __init__(self,eid,ename,sal):
#         self.eid=eid
#         self.ename=ename
#         self.sal=sal
#
#     def __str__(self):
#         return('EmpId:{} EmpName:{} EmpSal:{}'.format(self.eid,self.ename,self.sal))
#
# e1=emp(101,'smith',10000)
# print(e1)

''' __del__ '''

# class myclass:
#     def __del__(self):
#         print('Destroyed')
#
# c1=myclass()
# c2=myclass()
# del c1
#
#
