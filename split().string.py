Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> s='hai python'
>>> s
'hai python'
>>> s.split('h')
['', 'ai pyt', 'on']
>>> s.rsplit('h')
['', 'ai pyt', 'on']
>>> 
>>> s='hello bello'
>>> s
'hello bello'
>>> s.split('l')
['he', '', 'o be', '', 'o']
>>> s.rsplit('l')
['he', '', 'o be', '', 'o']
>>> s.split('h',1)
['', 'ello bello']
>>> s.rsplit()
['hello', 'bello']
>>> s.rsplit('h',1)
['', 'ello bello']
