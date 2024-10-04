n=int(input("Enter the number\n"))
end=int(input("Enter the end value\n"))
print("Multiplication table of {} upto {} is:".format(n,end))
for i in range(1,end+1):
	print("{}x{}={}".format(n,i,n*i))

