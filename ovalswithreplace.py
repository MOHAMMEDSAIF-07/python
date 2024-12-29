input_str =input("enter the string : ")
vowels = "aeiouAEIOU"

for vowel in vowels:
    input_str = input_str.replace(vowel, '/')   

print(input_str)