# list type is another sequence type defined by the list class of python
# list allows you to add,delete or process elements in very simple ways
# similar to arrays
# ordered, changeable and allow duplicate values

# creating list

# list1=list()  # empty list
# print(list1)
#
# list2=list([22,31,61])
# print(list2)
#
# list3=(['tom','jerry','spyke'])
# print(list3)
#
# list4=list('python')
# print(list4)

# accessing elements in list

# l=[1,2,3,4,5]
# print(l[1])
# print(l[:5])

# operators

# list1=[2,3,4,5,1,35]
#
# print(2 in list1)
# print(2 not in list1)

# print(len(list1))
# print(min(list1))
# print(max(list1))
# print(sum(list1))

# slicing

# list=[11,33,40,44,7,1,100]
# print(list[0:5])
# print(list[3::2])
# print(list[::-1])

# + and * operators in list

# list1=[11,33]
# list2=[1,9]
#
# list3=list1 + list2
# print(list3)
#
# list4=[1,2,3,4]
# list5=list4*3
# print(list5)

# iterating list using loop

# l=[1,2,3,4,5]
#
# for i in l:
#     print(i,end=' ')
#
# list1=[2,3,4,1,32,4]
# #
# list1.append(19)  # add an elements  to the end of the list and returns none
# print(list1)
#
# print(list1.count(4))  #returns the number if times elements appear in the list
#
# list2=[99,54]
#
# list1.extend(list2)  # append all the elements in another list and returns none
# print(list1)
#
# print(list1.index(32))  #returns index of the first occurance of element in list
#
# list1.insert(1,25)  #insert an element at a given index
# print(list1)
#
# print(list1.pop(2))  #removes element at the given position and returns it
# print(list1)
#
# list1.remove(32)  #removes element and returns none
# print(list1)
#
# list1.reverse() # reverse the list and returns none
# print(list1)
#
# list1.sort()
# print(list1)

# list comprehension

# list1=[x for x in range(10)]
# print(list1)
#
# list1=[x+1 for x in range(10)]
# print(list1)
#
# list1=[x for x in range(10) if x%2==0]
# print(list1)


