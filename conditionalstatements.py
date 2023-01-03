# example 1
a=20

if a>10:
    print('True condition')
else:
    print('False condition')

#example 2

a=25
if a%2==0:
    print('Number is even')
else:
    print('Number is odd')

# multiple statements under if ,else block

if True:
    print('statement1')
    print('statement2')
    print('statement3')
else:
    print('statement4')
    print('statement5')
print('This is not part of if or else block')

# single statements in single line

print('welcome') if False else print('python')
print('welcome') if True else print('python')
print('welcome') if 10<20 else print('python')

# multiple statements in single line

{print('welcome1'),print('python1')} if True else {print('welcome2'),print('python2')}

# elif command in python
a=15
if a==10:
    print('Ten')
elif a==20:
    print('Twenty')
elif a==30:
    print('Thirty')
else:
    print('Not listed')

