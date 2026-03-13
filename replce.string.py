Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> s='hai python'
>>> s
'hai python'
>>> s.replace('h','k')
'kai pytkon'
>>> s.replace('h','k',1)
'kai python'
>>> s.replace('h','k',10)
'kai pytkon'
>>> s.replace('h','')
'ai pyton'
>>> s=s.replace('h','')
>>> s
'ai pyton'
>>> s.replace('h','k',s.count('p'))
'ai pyton'
>>> m=s.count('p')
>>> s.replace('h','k',m)
'ai pyton'
>>> 
>>> m
1
>>> s
'ai pyton'
>>> 
