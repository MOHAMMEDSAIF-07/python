e = []
for i in range(3):
    num = int(input(f"Enter {i+1} number: "))
    e.append(num)

print(e)

l = e[-1]
l2 = e[-2]

print(l)
print(l2)

if num % l2 == 0 | num % l == 0:
    print("true")
else:
    print("false")