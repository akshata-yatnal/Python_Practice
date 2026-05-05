#WAP TO PRINT THE SUM OF DIGIT PRESENT IN A GIVEN STRING:
s=input('enter any string:')
sum=0
for ele in s:
    if ele.isdigit():
        sum+=int(ele)
print(sum)
