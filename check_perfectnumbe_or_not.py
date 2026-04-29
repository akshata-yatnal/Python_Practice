#WAP TO CHECK THE GIVEN NUMBER IS PERFECT NUMBER OR NOT:

n=int(input('enter any number:'))
sumdiv=0
for i in range(1,n):
    if n%i==0:
        sumdiv+=i
if n==sumdiv:
    print('perfect number')
else:
    print('not perfect number:')
    
# other wise we can use condition (1,n//2+1) condition also becoz its easy to compare:
