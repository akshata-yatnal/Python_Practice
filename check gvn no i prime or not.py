num=5
count_fact=0
for val in range(1,num+1):
    if num%val==0:
        count_fact +=1
if count_fact ==2:
    print(f'{num}is prime number')
else:
    print(f'{num}is non-prime number')
