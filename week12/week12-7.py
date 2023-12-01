a =int(input())
print(a,end="")
if a%400==0:print(" is a leap year.")
elif a%100==0:print(" is not a leap year.")
elif a%4==0:print(" is a leap year.")
else:print(" is not a leap year.")
	