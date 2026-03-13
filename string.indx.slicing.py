Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s='hai python'
s
'hai python'
s[1]
'a'
>>> s[5]
'y'
>>> s[56]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    s[56]
IndexError: string index out of range
>>> s[-1]
'n'
>>> s[-5]
'y'
>>> s[4:9:1]
'pytho'
>>> s[4:9:2]
'pto'
>>> s[4:9:5]
'p'
>>> s[1:2:3]
'a'
>>> s[-5:-1:1]
'ytho'
>>> s[-1:-5:1]
''
>>> s[2:7:]
'i pyt'
>>> s[-3:-6:-1]
'hty'
>>> s[-2:-7:-2]
'otp'
>>> 'otp'
'otp'
>>> s[-2:-7:-2]
'otp'
>>> s[1:8:-2]
''
>>> s[1:8:-1]
''
>>> s[-1::-1]
'nohtyp iah'
>>> s[::-1]
'nohtyp iah'
