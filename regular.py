import re
s = "hellohellohowareyoudoing"
b = re.match("hello",s)
if b == True:
  print("yes")
else:
  print("no")

print(re.findall("hello",s))
print(re.sub("hello","bye",s))

s = "My marks are 45,78 and 90"
print(re.findall(r'\d+',s))
pattern = r'^[0-9]\d{9}$'
print(re.match(pattern,"8433258844̥"))

pattern1 = r'^[a-zA-Z0-9._]+@[a-z]+\.[a-z]{2,}$'
print(re.match(pattern1,"aashish123@gmail.com"))
 


