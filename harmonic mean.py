n=int(input("enter the number of elements : "))
e = []
for i in range(n):
    num = int(input(f"Enter {i+1} number: "))
    e.append(num)

s=0
for f in e:
     s += 1/f
     
h_m=n/s
    
print("average of list elements : ",h_m)