a,b=list(map(int,input().split()))
ans=0
for i in range(a,b+1):
	if i%3 ==0:ans+=i
print(ans,end="")
###########################################
n = int(input())
ans = 0
for i in range(1,n):
	ans+=i*(i+1)
print(ans)