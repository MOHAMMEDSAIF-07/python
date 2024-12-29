n=int(input("enter the number : "))
count=1
for i in range(2,n+1):
    if n%i==0:
        count +=1
        
if count==2:
    print(" prime number ")
else:
    print(" composite numbers ")