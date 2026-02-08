num=int(input("Enter a number:"))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
if num==sum:
    print("Number is armstrong",num)
else:
    print("Number is not armstrong",num)
