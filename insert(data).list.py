Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> l=[11,22,33]
>>> l.insert(1,100)
>>> l
[11, 100, 22, 33]
>>> l.insert(1,'hello')
>>> l
[11, 'hello', 100, 22, 33]
>>> l.insert(100,899)
>>> l
[11, 'hello', 100, 22, 33, 899]
>>> l.insert(-1,666)
>>> l
[11, 'hello', 100, 22, 33, 666, 899]
>>> l.insert(-1000,555)
>>> l
[555, 11, 'hello', 100, 22, 33, 666, 899]
