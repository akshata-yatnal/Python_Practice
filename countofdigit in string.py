

# for loop USING CDT:string
#WAP TO PRINT HOW MANY DIGITS ARE PRESENT IN GIVEN STRING:

s=input('enter any string:')
count=0
for ele in s:
    if ele.isdigit():
        count+=1
print(count)

# another way to write this programm is:

s=input('ente any string:')
count=0
for ele in s:
    if (ele >='0' and ele<='9'):
        count+=1
print(count)


