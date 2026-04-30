# for loop USING CDT: string
#WAP TO PRINT HOW MANY SPECIAL CHARCTERS ARE PRESENT IN GIVEN STRING:

s=input('enter any string:')
count=0
for ele in s:
    if not ele.isalnum():
        count+=1
print(count)



# or other way that without using isalnum():


s=input('enter any string:')
count=0
for ele in s:
    if ele.isalnum()==False:
        count+=1
print(count)



