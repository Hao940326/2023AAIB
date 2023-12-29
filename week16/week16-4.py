a ,b= list(map(int,input().split()))
print(a*a-b*b,end='')
#############################################
a=int(input())
b=int(input())
ans = a-b*6
print(ans//6,ans%6,end='')
############################################
a= int(input())
print(a//1000%10,end='')
##################################################
x,y=list(map(int,input().split()))
if x>0 and y>0:print(1)
if x<0 and y>0:print(2)
if x<0 and y<0:print(3)
if x>0 and y<0:print(4)
##############################################