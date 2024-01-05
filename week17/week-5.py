a,b=list(map(int,input().split()))
ans = a//b
if a%b >0:ans+=1
print(ans,end='')
####################################
a=list(map(int,input().split()))
ans = 0
for b in a:
	if b>0:ans+=b
print(ans,end='')
##########################################
x1,y1,x2,y2=list(map(int,input().split()))
ans=(x1-x2)*(y1-y2)
print(abs(ans),end='')
##########################################
a=list(map(int,input().split()))
print(f'[{min(a)},{max(a)}]',end='')