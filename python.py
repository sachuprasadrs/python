a=int(input("Enter 1st number\n"))
b=int(input("Enter 2nd number\n"))
c=int(input("Enter your choice:\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exponentiation\n6.Floor Division\n7.Modulus\n"))
if c==1:
	s=a+b
	print("sum=",s)
elif c==2:
	s=a-b
	print("Difference=",s)
elif c==3:
	s=a*b
	print("Product=",s)
elif c==4:
	s=a/b
	print("Quotient=",s)
elif c==5:
	s=a**b
	print("After Exponentiation=",s)
elif c==6:
	s=a//b
	print("After Floor Division",s)
elif c==7:
	s=a%b
	print("Remainder=",s)
else:
	print("Invalid Choice")
	

