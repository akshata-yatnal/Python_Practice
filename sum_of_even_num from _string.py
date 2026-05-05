#WAP TO PRINT THE SUM OF EVEN DIGIT PRESENT IN A GIVEN STRING:

s=input("enter any string:")
sum=0
for ele in s:
    if ele.isdigit():
        if int(ele)%2==0:
            sum+=int(ele)
print(sum)



#or we can write this type also:

s=input("enter any string:")
sum=0
for ele in s:
    if ele.isdigit() and int(ele)%2==0:
        sum+=int(ele)
print(sum)


#or we can write this type also:

s=input("enter any string:")
sum=0
for ele in s:
    if ele in '02468':
        sum+=int(ele)
print(sum)
