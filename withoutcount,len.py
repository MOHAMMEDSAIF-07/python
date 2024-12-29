user=input("enter your input : ")
count = 0
for temp in user:
    if temp == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 0:
        count += 1

print(f"no.of digits in'{user}' is {count}")