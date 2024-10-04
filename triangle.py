a=int(input("Enter length of first side\n"))
b=int(input("Enter length of second side\n"))
c=int(input("Enter length of third side\n"))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("Area=",area)

