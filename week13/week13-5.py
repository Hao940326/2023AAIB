#soit106_advance_003
a = list(map(int,input().split()))
for i in range(len(a)-1-1,-1,-1):
	print(a[i],end=" ")
print()
#soit106_advance_009
#1
a = input()
for i in range(len(a)-1,-1,-1):
	print(a[i],end="")
print()
#2
while a>0:
	print(a%10,end="")
	a=a//10
print()