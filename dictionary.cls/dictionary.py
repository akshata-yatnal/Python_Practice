Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> d1={100:'A',200:'B'}
>>> d1
{100: 'A', 200: 'B'}
>>> 100 in d1
True
>>> 300 in d1
False
>>> 'A' in d1
False
>>> 200 in d1
True
>>> 
>>> d1={100:'A',200:'B'}
>>> d2={300:'C',400:'D'}
>>> d1==d2
False
>>> d1+d2
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    d1+d2
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
>>> d1-d2
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    d1-d2
TypeError: unsupported operand type(s) for -: 'dict' and 'dict'
>>> d1*d2
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    d1*d2
TypeError: unsupported operand type(s) for *: 'dict' and 'dict'
>>> # so with two dicts we cant perform any aritmatic on 2 dictionaries
>>> d3=(d1==d2)
>>> d3
False
>>> d4={100:'A',200:'B'}
>>> d5={100:'A',200:'B'}
>>> d4==d5
True
