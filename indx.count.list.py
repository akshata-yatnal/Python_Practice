Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> l=[11,11,44,66,33,22]
>>> l.index(11)
0
>>> l.index(11,2)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    l.index(11,2)
ValueError: 11 is not in list
>>> l.index(110)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    l.index(110)
ValueError: 110 is not in list
>>> l.index(11)
0
>>> l
[11, 11, 44, 66, 33, 22]
>>> l.index(11)
0
>>> l.count(11)
2
>>> l.count(110)
0
