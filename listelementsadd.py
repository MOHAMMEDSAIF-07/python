n=int(input("enter the number of elements : "))
e = []
for i in range(n):
    num = int(input(f"Enter {i+1} number: "))
    e.append(num)

s=0
for f in e:
     s +=f
    
print("Addition of list elements : ",s)