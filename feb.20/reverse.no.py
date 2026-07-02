n=int(input("enter number:"))
revere=0
while num>0:
    digit=num%10
    reverse=reverse*10+digit
    num=num//10
print("revered number:",reverse)
