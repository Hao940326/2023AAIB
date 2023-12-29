a= int(input())
ans=0
for i in range(1,1001):
	if i*i ==a:
		ans =i
print(ans,end='')
###################################
a,b=list(map(int,input().split()))
ans=0
for n in range(a,b+1):
	bad=0
	for i in range(2,int(n**0.5)+1):
		if n%i==0:bad =1
	if bad == 0:ans +=1
print(ans)
####################################
a=list(map(int,input().split()))
a.sort()
ans = a[2]*100+a[1]*10+a[0]+1
print(ans,end='')