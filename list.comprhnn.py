l1=[10,20,30,40]
l2=[30,40,50,60]
l3=[i for i in l1 if i not in l2]
print(l3)

l4=[i for i in l1 if i in l2]
print(l4)
