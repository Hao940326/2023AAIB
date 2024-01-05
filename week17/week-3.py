k=int(input())
total = 0
for i in range (1,k):
	total += i
	if total>k:
		ans = i
		break
print(ans,end='')
	
##################################
n= int(input())
total = 0
for i in range(n+1):
	total+=2*i+1
print(f'f({n})=',end='')
print(total,end='')