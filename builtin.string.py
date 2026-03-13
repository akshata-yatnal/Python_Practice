Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> s='hai'
>>> s
'hai'
>>> s.islower()
True
>>> s.isupper()
False
>>> s.istitle()
False
>>> 
>>> s='Hai'
>>> s
'Hai'
>>> s.isupper()
False
>>> s.islower()
False
>>> s.istitle()
True
>>> 
>>> s.[0:1:1].isupper()
SyntaxError: invalid syntax
>>> s1='Hai'
>>> s
'Hai'
>>> s.[0:1:1].isupper()
SyntaxError: invalid syntax
>>> s[0].isupper
<built-in method isupper of str object at 0x00007FF803A34B30>
>>> s[0].isupper()
True
>>> s[0:1:1].isupper()
True
