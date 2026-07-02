s='a4k3b2'
output=''
for ch in s:
    if ch.isalpha():
        x=ch
        output=output+ch
    else:
        d=int(ch)
        newc=chr(ord(x)+d)
        output=output+newc
print(output)
