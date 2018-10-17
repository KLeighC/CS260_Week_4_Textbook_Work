## Write a function revstring(mystr) that uses a stack to reverse the characters in a string

from Stack_Class_definition import Stack


def revstring(mystring):
    revStack = Stack()
    mylist = list(mystring)
    newlist = []

    for i in range(0, len(mystring)):
        revStack.push(mylist[i])

    for i in range(0,revStack.size()):
        newlist.append(revStack.pop())

    revWord = '%s'*len(newlist) % tuple(newlist)
    return revWord



s = 'watermelon'
z = revstring(s)

r = 'Happy Birthday'
q = revstring(r)
print(s)
print(z)

print(r)
print(q)

""" Code from textbook to test my code:

from test import testEqual
from pythonds.basic.stack import Stack

def revstring(mystring):
    revStack = Stack()
    mylist = list(mystring)
    newlist = []

    for i in range(0, len(mystring)):
        revStack.push(mylist[i])

    for i in range(0,revStack.size()):
        newlist.append(revStack.pop())

    revWord = '%s'*len(newlist) % tuple(newlist)
    return revWord

testEqual(revstring('apple'),'elppa')
testEqual(revstring('x'),'x')
testEqual(revstring('1234567890'),'0987654321')"""