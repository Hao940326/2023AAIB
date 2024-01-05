a= list(map(int,input().split()))
for i in range(10-1,-1,-1):	
	print(a[i],end=' ')
#################################
a=int(input())
print(int(1.2*60*60/a),end='')
##################################
a= int(input())
ans=0
for i in range(1,a+1):
	if a%i==0:
		ans+=i
print(ans,end='') 

#######################################
a = int(input())
ten=1
while a>0:
	print(a%10*ten,end=' ')
	ten = ten*10
	a=a//10