s=input('enter any string value:')
d={}
for ch in s:
    d[ch]=d.get(ch,0)+1
for k,v in d.items():
    print(k,'occur',v,'times')
    
