a=list(map(int,input().split()))
a.sort()
for i in range(10-1,-1,-1):
	print(a[i],end=' ')
#################################
a=list(map(int,input().split()))
fast = min(a)
for i in range(10):
	if a[i] == fast:
		ans =i
print(ans+1,int(1.2*60*60/fast))
##################################
a=int(input())
ans=0
for i in range(1,a+1):
	ans += 11*i
print(ans,end='')