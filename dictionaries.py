# Dictionary is a python data type that is used to store key value pairs
# enables you to quickly retrieve,add,remove,modify,values using keys
# mutable,changeble,ordered, not allow duplicate values

# friends = {'tom' : '111-222-333','jerry' : '666-33-111'}
# print(friends)

# retrieving,modifying and adding ele

# print(friends['tom']) #retrieving values
#
# friends['bob']='888-999-666'  #adding item
# print(friends)
#
# friends['bob']='888-999-777'   #modify values
# print(friends)
# #
# del friends['bob']  # delete element
# print(friends)

# looping items

# w={'a': '100',
#          'b': '200',
#          'c': '300',
#          'd':'400'}
#
# for x in w:
#     print(x,':',w[x])
#
# print(len(w))

#equality test

# d1={'nike':'45','bob':'35'}
# d2={'bob':'35','nike':'45'}
#
# print(d1==d2)
# print(d1!=d2)
#
friends={'tom' : '111-222-333','jerry' : '666-33-111','bob':'888-999-666'}

print(friends.popitem())  #returns randomly select item from dict and also remove
print(friends)

print(friends.clear())  # delete everything from dict

friends={'tom' : '111-222-333','jerry' : '666-33-111','bob':'888-999-666'}

print(friends.keys())  # returns keys in dict  as tuples
print(friends.values())  # returns values in dict  as tuples

print(friends.get('jerry')) # return value of key,if key is not found it returns none

print(friends.pop('tom'))
print(friends)
