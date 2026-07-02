num=int(input("enter number:"))
original=num
revere=0

while num>0:
    digit=num%10
    reverse=reverse*10+digit
    num=num//10
if original==reverse:
    print("palindrome")
else:
    print("not palindrome")
    
