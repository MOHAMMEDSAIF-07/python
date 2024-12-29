password = "hi1234"
ma=4
a=0

while a<ma:
    user = input("Enter your password: ")

    if user == password:
        print("Password accepted. Welcome")
        break  
    else:
        a+=1
        print(f"Incorrect password .you have {ma-a} attempts left")

if a==ma:
    print('two many incorrect attempts')