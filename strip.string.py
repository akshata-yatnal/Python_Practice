Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 'hai'
'hai'
>>> 'hai'.strip()
'hai'
>>> '.......hai......'.strip('.')
'hai'
>>> '    hai.......''.strip('.').strip()
SyntaxError: unterminated string literal (detected at line 1)
>>> '    hai.......'.strip('.').strip()
'hai'
>>> '.......hai.....'.strip()
'.......hai.....'
>>> '.......hai.....'.strip('.')
'hai'
>>> KeyboardInterrupt
>>> '.......hai.....'.strip('.').strip()
'hai'
>>> '.......hai.....'.rstrip()
'.......hai.....'
>>> '.......hai.....'.rstrip('.')
'.......hai'
>>> '.......hai.....'.lstrip('.')
'hai.....'
