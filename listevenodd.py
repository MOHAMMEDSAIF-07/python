M=[]
r=int(input("enter number of elements"))

for i in range(r):
        u=int(input(f"enter {i+1} element"))
        M.append(u)

o=[]
e=[]
for t in M:
    if t%2==0:
        e.append(t)
    else:
        o.append(t)
        
print(f"\n{e} even elements.No of elements {len(e)} \n")
print(f"{o} odd elements.No of elements {len(o)} \n")
print("Given list",M)
print("number of elements in the list",len(M))