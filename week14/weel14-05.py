a = list(map(int,input().split()))
ans =1
print("Enter the number of values to be processed: ",end="")
for i in range(1,len(a)):
	print("Enter a value: ",end='')
	ans*=a[i]
print("Product of the",a[0],"values is",ans,end='')
##############################
print(abs(int(input()))-2,end='')
##############################
a = int(input())
if a == 2:print(28,end='')
elif a==4 or a==6 or a==9 or a==11:print(30,end='')
else:print(31,end='')