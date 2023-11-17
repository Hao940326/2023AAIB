a = list(map(int,input().split()))
ans=max(a)
print(ans)

if a[0]>=a[1]and a[0]>=a[2]: ans =a[0]
if a[0]<=a[1]and a[0]>=a[2]: ans =a[1] 
if a[0]<=a[1]and a[1]<=a[2]: ans =a[2]