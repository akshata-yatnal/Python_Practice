n=int(input('enter no of students:'))
d={}
for i in range(n):
    name=input("enter student name:")
    marks=int(input("enter student marks:"))
    d[name]=marks
print("student data insertion completed")
print('*' *30)
print('name', '\t\t', 'marks')
print('*' *30)
for k,v in d.items():
    print(k,'\t\t',v)
    
