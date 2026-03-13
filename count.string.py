Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> S='Hai python'
>>> s.split()
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    s.split()
NameError: name 's' is not defined. Did you mean: 'S'?
>>> s
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    s
NameError: name 's' is not defined. Did you mean: 'S'?
>>> s='Hai python'
>>> s
'Hai python'
>>> s.split()
['Hai', 'python']
>>> s.split('h')
['Hai pyt', 'on']
>>> s.split('H')
['', 'ai python']
>>> s='hello bello'
>>> s
'hello bello'
>>> count('l')
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    count('l')
NameError: name 'count' is not defined. Did you mean: 'round'?
>>> s.count('l',5)
2
>>> s.count('l')
4
>>> s.count('l',5,7)
0
>>> s.count('l',9)
1
>>> s.count('ll',5)
1
>>> s.count('l',5,9)
1
