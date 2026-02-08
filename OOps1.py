def union_set(a,b):
  return a.union(b)
def intersection_set(a,b):
  return a.intersection(b)
def difference_set(a,b):
  return a.difference(b)
def symm_set(a,b):
  return a.symmetric_difference(b)
a = set(map(int,input("Enter set A elements seperated by space:").split()))
b = set(map(int,input("Enter set B elements seperated by space:").split()))

while True:
  print("1.Union")
  print("2.Intersection")
  print("3.Difference")
  print("4.Symmetric Difference")
  print("5.Exit")

  try:
    ch = int(input("Enter choice:"))

    if ch == 1:
      print("Union is:",union_set(a,b))
    elif ch ==2 :
      print("Intersection is:",intersection_set(a,b))
    elif ch ==3:
      print("Difference is:",difference_set(a,b))
    elif ch == 4:
      print("Symmetric Difference is:",symm_set(a,b))
    elif ch==5:
      break
    else:
      print("Inavlid Choice")
  except ValueError:
    print("Input a Valid Number")


