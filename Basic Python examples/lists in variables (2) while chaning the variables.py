Python 3.4.4 (v3.4.4:737efcadf5a6, Dec 20 2015, 20:20:57) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ListA = [1, 2, 3]
>>> ListB = [1, 2, 3]
>>> print('ListA =', ListA, 'ListB =', ListB)
ListA = [1, 2, 3] ListB = [1, 2, 3]
>>> ListA[1] = 1000
>>> print('ListA =', ListA, 'ListB =', ListB)
ListA = [1, 1000, 3] ListB = [1, 2, 3]
>>> 
=============================== RESTART: Shell ===============================
>>> listA = [1, 2, 3]
>>> listB = ListA
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    listB = ListA
NameError: name 'ListA' is not defined
>>> 
=============================== RESTART: Shell ===============================
>>> listA = [1, 2, 3]
>>> listB = listA
>>> print('listA =', listA, 'listB =', listB)
listA = [1, 2, 3] listB = [1, 2, 3]
>>> listA[1] = 1000
>>> print('listA =', listA, 'listB =', listB)
listA = [1, 1000, 3] listB = [1, 1000, 3]
>>> listB[2] = 75
>>> print('ListA =', ListA, 'ListB =', ListB)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print('ListA =', ListA, 'ListB =', ListB)
NameError: name 'ListA' is not defined
>>> print('listA =', listA, 'listB =', listB)
listA = [1, 1000, 75] listB = [1, 1000, 75]
>>> 
