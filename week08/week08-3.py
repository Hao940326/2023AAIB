a = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29]
n = len(a)
for i  in range(1,n):#this circle is start from 1
  print("Check",a[i],a[i-1])
  if a[i] - a[i-1] !=a[1]-a[0]:
    print("fail",a[i],a[i-1])
print("CodeCheckEnd")
