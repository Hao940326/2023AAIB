s = '00111'
n=len(s)
ans = 0
zero = 0
one = 0
for i in range(n):
  if s[i]=='1':one +=1
for i in range(n-1):
  if s[i] =='0':
    zero += 1
  if s[i] == '1':
    one -= 1
  ans=max(ans,zero+one)
print(ans)