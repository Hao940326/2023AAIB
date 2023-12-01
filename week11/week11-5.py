n = int(input())
for i in range(2,n+1,2):
	print(i,end=" ")

############################
a=list(map(int,input().split()))
print(min(a))
#######################
a=list(map(int,input().split()))

for i in range(6):
	print(a[i]*a[i]*a[i])

###################################
n = int(input())
ans = 0
for i in range(1,n+1):
	ans+=i*i
print(ans,end="")