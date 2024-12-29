M=[]
r=int(input("enter number of elements"))

for i in range(r):
        u=int(input(f"enter {i+1} element"))
        M.append(u)

e=[]
for t in M:
    if t%2==0:
        e.append(t)
add=0
for temp in e:
    temp *= temp
    add +=temp
        
print(f"\n{e} even elements.\n")
print("Given list",M)
print("addition of even numbers in the given list",add)