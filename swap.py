a=10
b=5
x=a
y=b
print("Swap with new variable\n\n")
print("Value of a before swap:",a)
print("Value of b before swap:",b)
temp=a
a=b
b=temp
print("Value of a after swap:",a)
print("Value of b after swap:",b)

print("Swap without new variable\n\n")
a=10
b=5
print("Value of a before swap:",a)
print("Value of b before swap:",b)
a=a+b
b=a-b
a=a-b
print("Value of a after swap:",a)
print("Value of b after swap:",b)
