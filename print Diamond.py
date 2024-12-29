n=int(input("enter number of lines : "))
a=" *"
b=" "
for i in range(1,n+1):
    print(b*(n-i),a*i)
for j in range(n,0,-1):
    x=j-1
    print(b*(n-x),a*x)