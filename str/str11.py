s='ABCDXXXDDDYYEEEYYY'
d={}
for ch in s:
    d[ch]=d.get(ch,0)+1
for k,v in d.items():
    print('{} occurrs {}time'.format(k,v))
