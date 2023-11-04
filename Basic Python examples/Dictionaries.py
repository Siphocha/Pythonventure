Python 3.4.4 (v3.4.4:737efcadf5a6, Dec 20 2015, 20:20:57) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> age = {'Mary': 10, 'Sanjay': 8}
>>> print(age)
{'Mary': 10, 'Sanjay': 8}
>>> age['Owen'] = 11
>>> print(age)
{'Mary': 10, 'Owen': 11, 'Sanjay': 8}
>>> age['Owen'] = 12
>>> print(age)
{'Mary': 10, 'Owen': 12, 'Sanjay': 8}
>>> del age['Owen']
>>> print(age)
{'Mary': 10, 'Sanjay': 8}
>>> 
