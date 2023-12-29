a = input()
if a.isupper():ans="U"
elif a.islower():ans="L"
elif a.isdigit():ans="D"
else:ans="O"
print(ans,end="")
#####################################
a = int(input())
print((a-1)%7,end='')
######################################
a = list(map(int,input().split()))
print(a[0]*50+a[1]*5+a[2]*1,end='')
#######################################
a =input()
print(a[0],end='')