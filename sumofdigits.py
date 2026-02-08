def func(n):
    if n==0:
        return 0
    else:
        num=n%10
        digit=func(n//10)
        return num+digit
print(func(120))   