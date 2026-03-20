marks=int(input('enter obtained mark:'))
if marks<0 or marks>100:
    print('Invalid marks')
elif marks>=90:
    print('Grade A+')
elif marks>=80:
    print('Grade A')
elif marks>=70:
    print('Grade B')
elif marks>=60:
    print('Grade C')
else:
    print('fail')
    
   
