def fact(num):
    result=1
    while num>=1:
        result=result*num
        num=num-1
    return result
print('the factorial of 3 is:',fact(3))
print('the factorial of 5 is:',fact(5))

for i in range(1,6):
    print('the factorial of ',i,'is',fact(i))




