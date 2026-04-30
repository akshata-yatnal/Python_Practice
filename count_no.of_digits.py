#WAP TO count number of digits in a number:

n=int(input('enter any nuber:'))
count=0
for i in range(len(str(n))):
    count+=1
print(count)
