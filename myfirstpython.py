#python trials script
print('basic loop example...')
a=0
for i in xrange(10):
    a=a+i
print('a='+str(a))

#redundant parenthesis
if ((a>10)):
    print('a>10')
elif a>5:
    print('a>5... never displayed...')
#FIXME test if fixme is found

#collapsing if statementsmistake
if a>10:
    if a>20:
        print('a est high')
a=0
for i in xrange(10):
    a=a+i
print('a='+str(a))

a=0
for i in xrange(10):
    a=a+i
print('a='+str(a))
a=0
for i in xrange(10):
    a=a+i
print('a='+str(a))

