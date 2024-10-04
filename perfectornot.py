num=int(input("Enter the number:\n"))
sum=0
for i in range(1,num):
	if num%i==0:
		sum=sum+i
if sum==num:
	print("Number is perfect\n")
else:
	print("Number is not perfect\n")
