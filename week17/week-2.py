a= int(input())
a=abs(a)
if a>=1000:
	print(a//1000)
elif a>=100:
	print(a//100)
elif a>=10:
	print(a//10)
else:
	print(a)
##########################################
a=input()
for i in range(len(a)):
	if i!=0 and (len(a)-i)%3==0:
		print(',',end='')
	print(a[i],end='')
#############################################
a=int(input())
h=a//3600
m=a//60%60
n=a%60
print(f'{h:02}:{m:02}:{n:02}',end='')