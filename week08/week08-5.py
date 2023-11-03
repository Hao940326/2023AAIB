a = [3,0,1,8,7,2,5,4,6,9]
n = len(a)
print(a)
for k in range(n):
  for i in range(1,n):
    if a[i]<a[i-1]:
      a[i],a[i-1] = a[i-1],a[i]
print(a)