d={100:'A',200:'B',300:'C',400:'D'}
key=int(input('enter key to find value:'))
if key in d:
    print('the corresponding value:',d.get(kye))
else:
    print('the specified key is not available')
