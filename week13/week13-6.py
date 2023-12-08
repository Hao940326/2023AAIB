#soit106_advance_007
a = input()
if a[0]==a[3] and a[1]==a[2]:
	print("YES")
else:print("NO")
#soit106_advance_010
a = list(map(int,input().split()))
for i in range(1,len(a)):
	print(a[i]*a[i],end=",")
print()
##soit106_advance_012
a = list(map(int,input().split()))
ans =0
for i in range(len(a)-2):
	if a[i] == a[-1]:
		ans +=1
print(ans)