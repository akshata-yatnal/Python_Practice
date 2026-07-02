d={100:'durga,200:''ravi',300:'shiva'}
key=int(input('enter key to find value:'))
if key in d:
    print('the corresponding value:',d[key])
else:
    print('the specified key is not available')
    
