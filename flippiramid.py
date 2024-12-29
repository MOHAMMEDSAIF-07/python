n = int(input("enter no.of lines : "))
a = " *"
b = " "
for i in range(n,0,-1):
    print(b*(n-i),a*i)