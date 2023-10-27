a = 12345
ans = 0
while(a>0):
  ans = ans*10+a%10

  print(a%10,"現在的a是:",a,"現在的a%10:",a%10,"現在的ans:",ans)
  a = a//10
print("ans:",ans)