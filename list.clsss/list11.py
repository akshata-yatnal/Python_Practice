Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> l=[23,54,65,75]
>>> l[1]
54
>>> l[1]=54
>>> l[1]
54
>>> l[2]
65
>>> l[:3:2]
[23, 65]
>>> l[-2::-2]
[65, 23]
>>> L[1]=100
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    L[1]=100
NameError: name 'L' is not defined. Did you mean: 'l'?
>>> l[1]=100
>>> 
>>> l=[23,54,65,75]
>>> l
[23, 54, 65, 75]
>>> l[1]=100
>>> l
[23, 100, 65, 75]
>>> 
>>> l=[10,[25,60],70]
>>> l
[10, [25, 60], 70]
>>> del[1]
SyntaxError: cannot delete literal
>>> del l[1]
>>> l
[10, 70]
>>> l
[10, 70]
>>> l[1][-1]
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    l[1][-1]
TypeError: 'int' object is not subscriptable
