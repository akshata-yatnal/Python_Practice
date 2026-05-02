# for loop USING CDT:
# for loop  CDT:CTIONARY CDI
d= {11:22,'hi':(22,33)}
for ele in d:
    print(ele)

 # using one variable on items(it will extract element)

d= {11:22,'hi':(22,33)}
print(d.items)
for ele in d.items():
    print(ele)


#using 2 variables on items(it will extract key first and value second variable):

d= {11:22,'hi':(22,33)}
for key,value in d.items():
    print(key ,value)
    
