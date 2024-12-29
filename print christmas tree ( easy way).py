n = 4
a = " *"
b = " "
for i in range(1, n + 1):
    print(b * (n - i) + a * i)
    
for j in range(1, n):
    print(b*(n-2)+a*(n-2))
    
print(a*n)