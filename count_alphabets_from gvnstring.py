# for loop USING CDT:
#WAP TO PRINT HOW MANY ALPHABETS ARE PRESENT IN GIVEN STRING:

s=input('enter any string:')
count=0
for ele in s:
    if ele.isalpha():
        count+=1
print(count)

# without using is.alpha():

s=input('enter any string:')
count=0
for ele in s:
    if (ele >='a' and ele<='z') or (ele >='A' and ele<='Z'):
        count+=1
print(count)
