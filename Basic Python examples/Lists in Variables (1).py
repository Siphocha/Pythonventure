Python 3.4.4 (v3.4.4:737efcadf5a6, Dec 20 2015, 20:20:57) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = 2
>>> b = a
>>> print('a =', a, 'b =', b)
a = 2 b = 2
>>> a = 100
>>> print('a=', a, 'b=', b)
a= 100 b= 2
>>> b =22
>>> 
=============================== RESTART: Shell ===============================
>>> a = 2
>>> b = a
>>> print('a =', a, 'b =', b)
a = 2 b = 2
>>> a = 100
>>> print('a=', a, 'b=', b)
a= 100 b= 2
>>> b = 22
>>> print('a=', a, 'b=', b)
a= 100 b= 22
>>> 
