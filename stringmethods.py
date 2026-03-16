Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> s='hai python'
>>> s
'hai python'
>>> s.index('h')
0
>>> s.portion('a')
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    s.portion('a')
AttributeError: 'str' object has no attribute 'portion'. Did you mean: 'partition'?
>>> s.partition('a')
('h', 'a', 'i python')
>>> ('h', 'a', 'i python')
('h', 'a', 'i python')
>>> s.partition('h')
('', 'h', 'ai python')
>>> s.partition('ho')
('hai pyt', 'ho', 'n')
>>> s.index('py')
4
>>> 'my salary is {} per month'.format(20000000000000.2380)
'my salary is 20000000000000.24 per month'
>>> '#'.join('bye')
'b#y#e'
>>> '#'.join(['bye','hello','hai'])
'bye#hello#hai'
>>> '#'.join(['bye','hello','hai',90])
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    '#'.join(['bye','hello','hai',90])
TypeError: sequence item 3: expected str instance, int found
>>> '#'.join(['bye','hello','hai','90'])
'bye#hello#hai#90'
