n=int(input("enter a number :"))
a = n % 10
x = n // 10
b = x % 10
if (n%a == 0 and n%b ==0):
    print("TRUE")
else:
    print("FALSE")