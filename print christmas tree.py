n = int(input("enter the number : "))
m = n//2
a = " *"
b = " "
for i in range(1, n + 1):
    print(b * (n - i) + a * i)
    
for j in range(1, n):
    print(b*(m)+a*(m))

print(a*n)