n=int(input('enter no of student:'))
d={}
for i in range(n):
    name=input('enter name of student:')
    marks=int(input("enter marks of student:"))
    d[name]=marks
print('*'*45)
print('name','\t\t','marks')
print('*'*45)
for name in d:
    print(name,'\t\t',d[name])
