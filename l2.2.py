a=int(input('enter a value:'))
b=int(input('enter b value:'))
c=int(input('enter c value:'))
if a>b and a>c:
    print('a is larger value')
elif b>a and b>c:
    print('b is larger value')
elif c>a and c>b:
    print('c is larger value')
else:
    print('some values are equal')
    
