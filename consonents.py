input_str = input("enter the string : ")
vowels = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
output_str = ""

n=1
for temp in input_str:
    if temp in vowels:
        output_str += str(n)
        n+=1
    else:
        output_str += temp

print(output_str)