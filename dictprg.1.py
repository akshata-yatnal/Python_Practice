''''d=eval(input("enter any dictionary:"))
sum=0
for item in d.items():
    sum=sum+item[1]
print('the sum of values:',sum)'''

d=eval(input("enter any dictionary:"))
print('the sum of values:',sum(d.values()))
      
