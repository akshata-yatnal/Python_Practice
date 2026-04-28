s=input('enter any string value:')
vowel={'a','e','i','o','u'}
d={}
for ch in s:
    if ch in vowel:
        d[ch]=d.get(ch,0)+1
for k,v in d.items():
    print(k,'occurrd',v,'times')

   
    
