n1=int(input("enter first number:"))
n2=int(input("entera second number:"))
a=1 
p=0
c=0
for i in range(n1,n2+1):
    for j in range(2,i+1):
           if(i%j==0):
               a=a+1
           else:
               a=a

    if(a>2):
       print(i," is a composite number")
       c+=1
       
    else:
       print(i,"is a prime number")
       p+=1
    a=1

print("number of composite numbers : ",c)
print("number of  prime number : ",p)