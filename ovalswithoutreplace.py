input_str = "Hello, how are you doing today?"
vowels = "aeiouAEIOU"
output_str = ""

for char in input_str:
    if char in vowels:
        output_str += '/'
    else:
        output_str += char

print(output_str)