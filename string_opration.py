'''
string is a collection of characters, we can write that using double quotes or single quotes
'''

# approach 1

name = 'John'
print(name)

# approach 2

name1 = str('welcome')
print(name1)

'''
stings are immutable, once string is created it can't be modified
'''

'''
id(): Every object in python is stored somewhere in memory.we can use id() to get memory address.
'''

# str1='welcome'
# str2='welcome'
#
# print(id(str1))  #1929699160240
# print(id(str2))  #1929699160240
#
# str2=str2+'to python'
#
# print(id(str1))  #1929699160240
# print(id(str2))  #1929703846848


# +(concatenation) and * (repeating multiple times)

# str='welcome '
# print(str+"to programing")
# print(str*3)
#
# # slicing  [start:end]
#
# str='welcome'
#
# print(str[1:3])
# print(str[:6])
# print(str[:])

'''
ord()-function returns character represented by a ASCII character
chr()-............................................ASCII number
'''

# print(ord('Z'))
# print(chr(90))
#
# print(len('hello'))   # length of the string
# print(max('abc'))     # character having highest ASCII value
# print(min('abc'))     # .................lowest ASCII value

# in and not in operator

# s1='welcome'
# print('come' in s1)
# print('abc' not in s1)

# string comparison
# compares string using ASCII value of the characters

# print('tim'=='tie')
# print('free'!='freedom')
# print('arrow'> 'aron')
# print('right'>='left')
# print('teeth'<'tee')
# print('yellow'<='fellow')
# print('abc'>' ')

# iterating string using for loop

# s = 'hello'
# for i in s:
#     print(s)

# Testing strings

# a = 'welcome to python'

# print(a.isalnum())   #Returns true if string is alphanumeric

# print('welcome'.isalpha())  # Returns true if string contain only alphabates

# print('2012'.isdigit())   # Return true if string contain only digits

# print('first number'.isidentifier())  #Return true if string is valid identifier

# print(a.islower())  #Return true if string in lowercase

# print('WELCOME'.isupper())  # Return true if string in uppercase

# print(' '.isspace())  # Returns true if string contains only whitespace

# searching for substrings

# s='welcome to python'
#
# print(s.endswith('thon'))
# print(s.startswith('good'))
# print(s.find('come'))
# print(s.find('become'))
# print(s.rfind('o'))  # Returns highest index from where s start in the string,if string not found returns -1
# print(s.count('o'))  # Returns highest index from where s start in the string,if string not found returns -1


#converting strings

# s='string in PYTHON'
#
# s1=s.capitalize()
# print(s1)
#
# s2=s.title()
# print(s2)
#
# s3=s.lower()
# print(s3)
#
# s4=s.upper()
# print(s4)
#
# s5=s.swapcase()
# print(s5)
#
# s6=s.replace('in','on')
# print(s6)
#
#
