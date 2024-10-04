r=int(input("Enter a range\n"))
isprime=True
for num in range(2,r+1):
	if num>1:
		isprime=True
		for i in range(2,num):
			if num%i==0:
				isprime=False
				break
	if isprime:
		print(num)
