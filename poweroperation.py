n=[]
y=int(input("enter number of elements : "))
p=int(input("enter the power value : "))
for i in range(1,y+1):
    x=(i**p)
    n.append(x)

print(n)