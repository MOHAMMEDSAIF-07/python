n=int(input("enter the number of elements : "))
e = []
for i in range(n):
    num = int(input(f"Enter {i+1} number: "))
    e.append(num)

p=1
for f in e:
     p *=f
    
print("multiplication of list elements : ",p)