Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> l=[11,22,33]
>>> l,extend(90)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    l,extend(90)
NameError: name 'extend' is not defined
>>> l.extend('hai')
>>> l
[11, 22, 33, 'h', 'a', 'i']
>>> l.extend([89,'hai'])
>>> l
[11, 22, 33, 'h', 'a', 'i', 89, 'hai']
>>> l.extend((10,20,'oyy',78))
>>> l
[11, 22, 33, 'h', 'a', 'i', 89, 'hai', 10, 20, 'oyy', 78]
