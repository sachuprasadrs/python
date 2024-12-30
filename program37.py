def gcd(n1,n2):
	if(n2!=0):
		return gcd(n2,n1%n2)
	else:
		return n1
n1=int(input("Enter 1st number:"))
n2=int(input("Enter 2nd number:"))

gcd_re=gcd(n1,n2)
print(gcd_re)
