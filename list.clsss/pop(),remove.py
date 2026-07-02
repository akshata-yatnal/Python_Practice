Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> l=[555,11,'hello',100,22,33,666,899]
>>> l.pop()
899
>>> l
[555, 11, 'hello', 100, 22, 33, 666]
>>> l.pop(22)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    l.pop(22)
IndexError: pop index out of range
>>> l.append(100)
>>> l
[555, 11, 'hello', 100, 22, 33, 666, 100]
>>> l.remove(100)
>>> l
[555, 11, 'hello', 22, 33, 666, 100]
>>> L=[11,20,[80,90],'HAI']
>>> NCL=L
>>> SCL=L.COPY()
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    SCL=L.COPY()
AttributeError: 'list' object has no attribute 'COPY'
>>> L=[11,20,[80,90],'HAI']
... NCL=L
... SCL=L.COPY()
SyntaxError: multiple statements found while compiling a single statement
